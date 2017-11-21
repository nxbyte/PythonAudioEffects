'''
	File: AudioEffect.py
	Description: A python class to perform high level effects on a given input and outputing to a file
	Version: 1 (Tested to work with WAV files)

	How to use:

	from AudioLib.AudioEffect import AudioEffect

	AudioEffect.echo('input.wav', 'output.wav')
'''

from AudioProcessing import AudioProcessing

class AudioEffect(object):

	__slots__ = ()

	@staticmethod
	def darth_vader(input_path, output_path):
		'''Applies a Darth Vader effect to a given input'''
		print 'Not Implemented'

	@staticmethod
	def echo(input_path, output_path):
		'''Applies an echo effect to a given input'''

		sound = AudioProcessing(input_path)
		sound.set_echo(0.1)
		sound.save_to_file(output_path)

	@staticmethod
	def radio(input_path, output_path):
		'''Applies a radio effect to a given input'''
		print 'Not Implemented'

	staticmethod
	def robotic(input_path, output_path):
		'''Applies a robotic effect to a given input'''
		print 'Not Implemented'

	@staticmethod
	def ghost(input_path, output_path):
		'''Applies a ghostly halloween effect to a given input'''
		print 'Not Implemented'
