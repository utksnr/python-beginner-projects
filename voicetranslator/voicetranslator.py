import speech_recognition as sr
from translate import Translator
from gtts import gTTS
from playsound import playsound
import os

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Please speak to your mic.")
        audio = r.listen(source)
        try:
            speech_text=r.recognize_google(audio)
            print(speech_text)
            if(speech_text == "exit program"):
                break
        except sr.UnknownValueError:
            print("Could not understand you.")
        except sr.RequestError:
            print("Program down")

        translator=Translator(to_lang="Turkish")
        out=translator.translate(speech_text)
        print(out)

        voice = gTTS(out,lang="tr")
        voice.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")


