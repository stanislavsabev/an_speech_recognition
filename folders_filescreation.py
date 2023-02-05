import os
import speech_recognition as sr
import siri


def foledrcreation():
    engine = siri.engine
    r = sr.Recognizer()

    siri.speak("Please say the name of the folder you want to create.")

    with sr.Microphone() as source:
        audio_text = r.listen(source)
        folder_name = r.recognize_google(audio_text)

    try:
        os.makedirs(folder_name)
        siri.speak("The folder has been created.")
    except FileExistsError:
        siri.speak("The folder already exists.")

    siri.speak("Please say the name of the file you want to create.")

    with sr.Microphone() as source:
        audio_text = r.listen(source)
        file_name = r.recognize_google(audio_text)

    file_path = os.path.join(folder_name, file_name)

    try:
        with open(file_path, "w", encoding="utf-8"):
            pass
        siri.speak("The file has been created.")
    except Exception as e:
        siri.speak(f"An error occurred while creating the file: {str(e)}")
