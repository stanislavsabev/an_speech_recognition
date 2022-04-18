from typing import Optional
import pyttsx3
import speech_recognition as sr 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice', voices[1].id)


class Siri:
    is_quiet = False


def go_quiet(value):
    Siri.is_quiet = value


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command(retry=False, cancel_noise=False) -> str:
    def _take_command():
        # It takes microphone input from the user and returns string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            if cancel_noise:
                print('Clearing the background noises..')
                r.adjust_for_ambient_noise(source,duration=1)
            r.pause_threshold = 1
            print("Listening...")
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f">> You said: {query}\n")    
        except Exception as e:
            return ''
        return query

    command = _take_command()
    if not command and retry and not Siri.is_quiet:
        while not command:
            speak("Say that again please!")
            command = _take_command()
    return command


def speak_and_take_command(audio, retry=False) -> str:
    speak(audio)
    return take_command(retry)
