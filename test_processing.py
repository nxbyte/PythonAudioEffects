
from AudioLib.AudioProcessing import AudioProcessing

sound1 = AudioProcessing('/Users/nextseto/GitHub/PythonAudioEffects/input.wav')

sound1.set_audio_speed(0.5)

sound1.set_audio_pitch(2)

sound1.set_reverse()

sound1.set_echo(1)

sound1.save_to_file('/Users/nextseto/Desktop/out.wav')
