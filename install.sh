#!/bin/bash
set -e

#brew install portaudio
#brew install flac
#brew install ffmpeg
# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg # https://github.com/openai/whisper

sudo apt-get install python3-all-dev
sudo apt-get install portaudio19-dev
sudo apt-get install python3-pyaudio

brew install portaudio
brew install flac
brew install ffmpeg


pip install openai
pip install soundfile
pip install pyaudio
pip install -U openai-whisper
pip install SpeechRecognition

pip install gtts
pip install playsound 
pip install tempfile

