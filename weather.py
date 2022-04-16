
from email.mime import audio
import speech_recognition as sr
from google_trans_new import google_translator

import pyttsx3 
recognizer=sr.Recognizer()
engine=pyttsx3.init()

with sr.Microphone() as source:
    print('Clearing the background noises..')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print('Waiting for your message')
    audio=recognizer.listen(source,timeout=1)
    print('Done recording') 

try:
    print('Recognizing')
    result=recognizer.recognize_google(audio,language='en')
except Exception as ex:
    print(ex) 

#Translation function
def trans():
    langinput=input('Type the language code you want to translate')
    translator=google_translator()
    translate_text=translator.translate(str(result),lang_tgt=str(langinput))
    print(translate_text)
    engine.say(str(translate_text))
    engine.runAndWait
    trans()