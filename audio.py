from scipy.signal import lfilter, butter
from scipy.io.wavfile import read,write
import numpy as np
from numpy import array, int16
import sys
from audioop import add
import wave

def input_wave(file,frames=256000): #File needs to be mono for this to work
    with wave.open(file,'rb') as wave_file:
        params=wave_file.getparams()
        audio=wave_file.readframes(frames)  
    return params, audio

def output_wave(wav, params, core, appendix):
    filename=core.replace('.wav','_{}.wav'.format(appendix)) #generates the new file
    with wave.open(filename,'wb') as wave_file:
        wave_file.setparams(params)
        wave_file.writeframes(wav)

def delay(audio_bytes,params,offset_ms):
    """sets the delay by offset milliseconds"""
    #calculate the number of bytes which corresponds to the offset in milliseconds
    offset= params.sampwidth*offset_ms*int(params.framerate/1000)
    #create silent audio by offset length
    beginning= b'\0'*offset
    #remove space from the end to compensate for blank audio. Audio must be samelength to add
    end = audio_bytes[:-offset]
    return add(audio_bytes, beginning+end, params.sampwidth)

def echo(sample_file):
    sample_params, sample_bytes = input_wave(sample_file)
    output_wave(delay(sample_bytes,sample_params,500), 
            sample_params, 'convert.wav','delay_effect')

def stretch(snd_array, factor, window_size, h):
    """ Stretches/shortens a sound, by some factor. """
    phase = np.zeros(window_size)
    hanning_window = np.hanning(window_size)
    result = np.zeros(int(len(snd_array) / factor + window_size))
    
    for i in np.arange(0, len(snd_array) - (window_size + h), h*factor):
        # Two potentially overlapping subarrays
        a1 = snd_array[int(i): int(i + window_size)]
        a2 = snd_array[int(i + h): int(i + window_size + h)]
        
        # The spectra of these arrays
        s1 = np.fft.fft(hanning_window * a1)
        s2 = np.fft.fft(hanning_window * a2)
        
        # Rephase all frequencies
        phase = (phase + np.angle(s2/s1)) % 2*np.pi
        
        a2_rephased = np.fft.ifft(np.abs(s2)*np.exp(1j*phase))
        i2 = int(i/factor)
        result[i2: i2 + window_size] += hanning_window*a2_rephased.real
    
    # normalize (16bit)
    result = ((2**(16-4)) * result/result.max())

    return result.astype('int16')


def set_audio_pitch(snd_array, n, window_size=2**13, h=2**11):
    """ Changes the pitch of a sound by ``n`` semitones. """
    factor = 2**(1.0 * n / 12.0)
    stretched = stretch(snd_array, 1.0/factor, window_size, h)
    return set_audio_speed(stretched[window_size:], factor)

def set_audio_speed(sound_array, speed_factor):
    sound_index = np.round(np.arange(0, len(sound_array), speed_factor))
    return sound_array[sound_index[sound_index < len(sound_array)].astype(int)]

def stereoToMono(audiodata):
    newaudiodata = []

    audiodata = audiodata.astype(float)

    for i in range(len(audiodata)):
        d = ((audiodata[i][0])/2) + ((audiodata[i][1])/2)
        newaudiodata.append(d)
    
    return np.array(newaudiodata, dtype='int16')

if __name__ == '__main__':
    '''
        Example: python audio.py sound.wav
    '''
    '''
    fs,audio = read(sys.argv[1])
    audio = stereoToMono(audio)
    filtered_signal = set_audio_speed(audio, 0.5)
    filtered_signal = set_audio_pitch(filtered_signal, 2)

    fname = sys.argv[1].split('.wav')[0] + '_new.wav'
    write(fname,fs,array(filtered_signal,dtype=int16))
    '''
    echo(sys.argv[1])