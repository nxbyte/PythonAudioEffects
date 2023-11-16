'''
    Usage  : python processing.py
    
    Input  : An input WAV file for processing
    Output : A processed WAV audio sample
    
    Note   : Please change the code below to fit your needs.
'''

import sys
sys.path.append('<path>/PythonAudioEffects')
# EXAMPLE: In my case it was, sys.path.append('/home/pixel22/Projects/PythonAudioEffects')
from AudioLib import AudioEffect
from AudioLib.AudioProcessing import AudioProcessing

sound1 = AudioProcessing('input.wav')

sound1.set_audio_speed(0.5)
sound1.set_audio_pitch(2)
sound1.set_reverse()
sound1.set_echo(1)

sound1.save_to_file('output.wav')
