'''
    Usage  : python effects.py
    
    Input  : An input WAV file for processing
    Output : Five processed WAV audio samples
    
    Note   : Please change the code below to fit your needs.
'''

from AudioLib import AudioEffect

input_file_path = 'input.wav'
output_filename = 'output'

AudioEffect.ghost(input_file_path, output_filename + '_ghost.wav')
AudioEffect.robotic(input_file_path, output_filename + '_robotic.wav')
AudioEffect.echo(input_file_path, output_filename + '_echo.wav')
AudioEffect.radio(input_file_path, output_filename + '_radio.wav')
AudioEffect.darth_vader(input_file_path, output_filename + '_vader.wav')
