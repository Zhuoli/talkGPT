import speech_recognition as sr
import os
import openai
import argparse
from gtts import gTTS
import tempfile
from playsound import playsound


LANGUAGES = {
    "en": "english",
    "zh-hans": "chinese"
}

def talk(language):
    print("\n\nListening...")
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        transcript = r.recognize_whisper(audio, language=language)
        print("WHISPER thinks you said: " + transcript)
        return transcript

def send_request(language, words):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0301",
      messages=[
        {"role": "user", "content": words}
      ]
    )
    return completion.choices[0].message["content"]

def speak(text,language):
  # Create a gTTS object with the text and language
  tts_object = gTTS(text=text, lang=language, slow=False)

  # Create a temporary file
  with tempfile.NamedTemporaryFile(delete=True) as fp:
      temp_filename = fp.name + ".mp3"
      
      # Save the converted speech to the temporary file
      tts_object.save(temp_filename)
      
      # Play the temporary file using playsound
      playsound(temp_filename)

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
  while True:
      input_words = talk(language)
      answer = send_request(language, input_words)
      print("GPT replied: " + answer)
      speak(answer, 'en')
