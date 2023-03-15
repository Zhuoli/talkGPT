#!/bin/bash
set -e
#brew install portaudio
#brew install flac
#brew install ffmpeg
sudo apt-get install python3-all-dev
sudo apt-get install portaudio19-dev
sudo apt-get install python3-pyaudio

pip install openai
pip install soundfile
pip install pyaudio
pip install -U openai-whisper
pip install SpeechRecognition

