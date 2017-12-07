'''
	File: AudioEffect.py
	Description: A python class to perform high level effects on a given input and outputing to a file
	Version: 1 (Tested to work with WAV files)

	How to use:

	from AudioLib import AudioEffect

	AudioEffect.echo('input.wav', 'output.wav')
'''

from AudioLib.AudioProcessing import AudioProcessing

class AudioEffect(object):

	__slots__ = ()

	@staticmethod
	def darth_vader(input_path, output_path):
		'''Applies a Darth Vader effect to a given input audio file'''
		sound = AudioProcessing(input_path)
		sound.set_audio_speed(.8)
		sound.set_echo(0.02)
		sound.set_lowpass(2500)
		sound.save_to_file(output_path)

	@staticmethod
	def echo(input_path, output_path):
		'''Applies an echo effect to a given input audio file'''
		sound = AudioProcessing(input_path)
		sound.set_echo(0.09)
		sound.save_to_file(output_path)

	@staticmethod
	def radio(input_path, output_path):
		'''Applies a radio effect to a given input audio file'''
		sound = AudioProcessing(input_path)
		sound.set_highpass(2000)
		sound.set_volume(4)
		sound.set_bandpass(50, 2600)
		sound.set_volume(2)
		sound.save_to_file(output_path)

	@staticmethod
	def robotic(input_path, output_path):
		'''Applies a robotic effect to a given input audio file'''
		sound = AudioProcessing(input_path)
		sound.set_volume(1.5)
		sound.set_echo(0.01)
		sound.set_bandpass(300, 4000)
		sound.save_to_file(output_path)

	@staticmethod
	def ghost(input_path, output_path):
		'''Applies a ghostly halloween effect to a given input audio file'''
		sound = AudioProcessing(input_path)
		sound.set_reverse()
		sound.set_echo(0.05)
		sound.set_reverse()
		sound.set_audio_speed(.70)
		sound.set_audio_pitch(2)
		sound.set_volume(8.0)
		sound.set_bandpass(50, 3200)
		sound.save_to_file(output_path)
