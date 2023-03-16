#!/bin/bash
set -e
<<<<<<< HEAD
#brew install portaudio
#brew install flac
#brew install ffmpeg
# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg # https://github.com/openai/whisper

sudo apt-get install python3-all-dev
sudo apt-get install portaudio19-dev
sudo apt-get install python3-pyaudio
=======
brew install portaudio
brew install flac
brew install ffmpeg
#sudo apt-get install python3-all-dev
#sudo apt-get install portaudio19-dev
#sudo apt-get install python3-pyaudio
>>>>>>> 5e721d82cc6d8e8295f714cd037fe51558338ae3

pip install openai
pip install soundfile
pip install pyaudio
pip install -U openai-whisper
pip install SpeechRecognition

pip install gtts
pip install playsound 
pip install tempfile

