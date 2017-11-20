from audioop import add
import wave
from scipy.signal import lfilter, butter
from scipy.io.wavfile import read,write
import numpy as np
from numpy import array, int16
import sys

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
    """version 1: delay after 'offset_ms' milliseconds"""
    #calculate the number of bytes which corresponds to the offset in milliseconds
    offset= params.sampwidth*offset_ms*int(params.framerate/1000)
    #create silent audio by offset length
    beginning= b'\0'*offset
    #remove space from the end to compensate for blank audio
    end = audio_bytes[:-offset]
    return add(audio_bytes, beginning+end, params.sampwidth)

if __name__ == '__main__':

    sample_params, sample_bytes = input_wave('convert.wav')
    output_wave(delay(sample_bytes,sample_params,500), 
            sample_params, 'convert.wav','delay_effect')