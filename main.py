import speech_recognition as sr
import os
import sys
import openai
import subprocess
import argparse


LANGUAGES = {
    "en": "english",
    "zh-hans": "chinese"
}
def print_error(text):
    red = "\033[31m"
    reset = "\033[0m"
    print(f"{red}{text}{reset}")

def talk(language):
    print("\n\nListening...")
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print(audio)
        transcript = r.recognize_whisper(audio, language=language)
        print(transcript)
        return transcript

def gpt_answer(language, words):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0301",
      messages=[
        {"role": "user", "content": words}
      ]
    )
    return completion.choices[0].message["content"]

OPENAI_API_KEY = "OPENAI_API_KEY"
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument(
        "--language",
        type=str,
        choices=sorted(LANGUAGES.keys()),
        default="en",
        metavar="LANGUAGE",
        help="language to talk, available: {%(choices)s}",
  )
  options = parser.parse_args()
  language = LANGUAGES[options.language]
  print(language)
  openai.api_key = os.getenv(OPENAI_API_KEY)
  if openai.api_key is None:
      print_error(OPENAI_API_KEY + " not found, please set it in environment variable")
      sys.exit(1)
  while True:
      input_words = talk(language)
      answer=gpt_answer(language, input_words)
      print(answer)
      voice = ""
      if language == "chinese":
          voice = "--voice Tingting"
      cmd_str = "say " + voice +  " \"" + answer.replace("\n", " ") + "\""
      subprocess.call(cmd_str, shell=True)
