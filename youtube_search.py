import speech_recognition as sr
import pyttsx3
import siri
import webbrowser





def open_video(video_name):
    url = f"https://www.youtube.com/results?search_query={video_name}"
    webbrowser.open(url)

def search_video():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            siri.speak("Say the name of the video you want to open:")
            audio_text = r.listen(source)
            print("Recognizing...")
            video_name = r.recognize_google(audio_text)
            print(f"You said: {video_name}")
            siri.speak(f"You said: {video_name}")

        siri.speak("Did I hear it correctly?")
        with sr.Microphone() as source:
            audio_text = r.listen(source)
            confirmation = r.recognize_google(audio_text)

        if "yes" in confirmation or "correct" in confirmation:
            break
        else:
            siri.speak("Let's try again.")

    open_video(video_name)
