'''
	File: AudioProcessing.py
	Description: A python class to perform low level DSP processing on a given input audio data
	Version: 1 (Tested to work with WAV files)

	How to use:

	from AudioLib.AudioProcessing import AudioProcessing

	# Read in WAV file into Python Class
	sound1 = AudioProcessing('input.wav')

	# Set the speed of the audio
	sound1.set_audio_speed(0.5)

	# Set the pitch of the audio
	sound1.set_audio_pitch(2)

	# Reverse the content of the audio
	sound1.set_reverse()

	# Add an echo to the audio
	sound1.set_echo(1)

	# Applies a bandpass filter between the (<low>, <high>) range of frequencies
	sound.set_bandpass(50, 2600)

	# Save the resulting processed audio data into a file
	sound1.save_to_file('out.wav')
'''

import sys, wave
import numpy as np
from numpy import array, int16
from scipy.signal import lfilter, butter
from scipy.io.wavfile import read,write
from scipy import signal


class AudioProcessing(object):

	__slots__ = ('audio_data', 'sample_freq')

	def __init__(self, input_audio_path):
		self.sample_freq, self.audio_data = read(input_audio_path)
		self.audio_data = AudioProcessing.convert_to_mono_audio(self.audio_data)

	def save_to_file(self, output_path):
		'''Writes a WAV file representation of the processed audio data'''
		write(output_path, self.sample_freq, array(self.audio_data, dtype = int16))

	def set_audio_speed(self, speed_factor):
		'''Sets the speed of the audio by a floating-point factor'''
		sound_index = np.round(np.arange(0, len(self.audio_data), speed_factor))
		self.audio_data = self.audio_data[sound_index[sound_index < len(self.audio_data)].astype(int)]

	def set_echo(self, delay):
		'''Applies an echo that is 0...<input audio duration in seconds> seconds from the beginning'''
		output_audio = np.zeros(len(self.audio_data))
		output_delay = delay * self.sample_freq

		for count, e in enumerate(self.audio_data):
			output_audio[count] = e + self.audio_data[count - int(output_delay)]

		self.audio_data = output_audio

	def set_volume(self, level):
		'''Sets the overall volume of the data via floating-point factor'''
		output_audio = np.zeros(len(self.audio_data))

		for count, e in enumerate(self.audio_data):
			output_audio[count] = (e * level)

		self.audio_data = output_audio

	def set_reverse(self):
		'''Reverses the audio'''
		self.audio_data = self.audio_data[::-1]

	def set_audio_pitch(self, n, window_size=2**13, h=2**11):
		'''Sets the pitch of the audio to a certain threshold'''
		factor = 2 ** (1.0 * n / 12.0)
		self._set_stretch(1.0 / factor, window_size, h)
		self.audio_data = self.audio_data[window_size:]
		self.set_audio_speed(factor)

	def _set_stretch(self, factor, window_size, h):
		phase = np.zeros(window_size)
		hanning_window = np.hanning(window_size)
		result = np.zeros(int(len(self.audio_data) / factor + window_size))

		for i in np.arange(0, len(self.audio_data) - (window_size + h), h*factor):
			# Two potentially overlapping subarrays
			a1 = self.audio_data[int(i): int(i + window_size)]
			a2 = self.audio_data[int(i + h): int(i + window_size + h)]

			# The spectra of these arrays
			s1 = np.fft.fft(hanning_window * a1)
			s2 = np.fft.fft(hanning_window * a2)

			# Rephase all frequencies
			phase = (phase + np.angle(s2/s1)) % 2*np.pi

			a2_rephased = np.fft.ifft(np.abs(s2)*np.exp(1j*phase))
			i2 = int(i / factor)
			result[i2: i2 + window_size] += hanning_window*a2_rephased.real

		# normalize (16bit)
		result = ((2 ** (16 - 4)) * result/result.max())
		self.audio_data = result.astype('int16')

	def set_lowpass(self, cutoff_low, order=5):
		'''Applies a low pass filter'''
		nyquist = self.sample_freq / 2.0
		cutoff = cutoff_low / nyquist
		x, y = signal.butter(order, cutoff, btype='lowpass', analog=False)
		self.audio_data = signal.filtfilt(x, y, self.audio_data)

	def set_highpass(self, cutoff_high, order=5):
		'''Applies a high pass filter'''
		nyquist = self.sample_freq / 2.0
		cutoff = cutoff_high / nyquist
		x, y = signal.butter(order, cutoff, btype='highpass', analog=False)
		self.audio_data = signal.filtfilt(x, y, self.audio_data)

	def set_bandpass(self, cutoff_low, cutoff_high, order=5):
		'''Applies a band pass filter'''
		cutoff = np.zeros(2)
		nyquist = self.sample_freq / 2.0
		cutoff[0] = cutoff_low / nyquist
		cutoff[1] = cutoff_high / nyquist
		x, y = signal.butter(order, cutoff, btype='bandpass', analog=False)
		self.audio_data = signal.filtfilt(x, y, self.audio_data)

	@staticmethod
	def convert_to_mono_audio(input_audio):
		'''Returns a numpy array that represents the mono version of a stereo input'''
		output_audio = []
		temp_audio = input_audio.astype(float)

		for e in temp_audio:
			output_audio.append((e[0] / 2) + (e[1] / 2))

		return np.array(output_audio, dtype = 'int16')
