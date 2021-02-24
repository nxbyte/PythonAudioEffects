# PythonAudioEffects

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/nextseto/PythonAudioEffects/master/LICENSE)

Many movies have special effects added to the visuals and the audio to set the tone for various scenes. In movies, editors use audio processing to apply effects to voice actors to make them seem more dramatic or to better fit the overall storyline. 

**PythonAudioEffects** is a python library that can manipulate audio files (Mono WAV) and apply: darth vader, echo, radio, robotic, and ghost effects onto audio. In addition to applying pre-built custom audio effects, the library also provides DSP operations to build even more effects!!

## Installation

### Requirements

  * Python 2.7 or 3.x
  * Windows, macOS or Linux
  * numpy: `pip install numpy`
  * scipy: `pip install scipy`

**Note:** [macOS users may need to setup using virtualenv.](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3)

## How to use

1. Clone the repository
2. Look at: `tests/effects.py` for processing a WAV file and generating different premade effects
3. Look at `tests/processing.py` to learn how to use the DSP operations for manipulating audio


## License

All **source code** in this repository is released under the MIT license. See LICENSE for details.

