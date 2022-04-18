import sys
import webbrowser

import datetime
import wikipedia
import os
import smtplib
from siri import speak
from siri import take_command
from translate import trans
import theday

song_number = 0
music_dir = 'songsforai'
songs = os.listdir(music_dir) 


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello Sir. how can I help you?")


def play_music():
    global song_number
    if 'previous song' in query:
        song_number -= 1
    elif 'next song' in query:
        song_number += 1
    print(songs[song_number])
    os.startfile(os.path.join(music_dir, songs[song_number]))


def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587 )
    server.ehlo()
    server.starttls()
    server.login('an20.olimpic@gmail.com', 'balgaria20!')
    server.sendmail('an20.olimpic@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    i = 0
    while True:
        # if i > 0:
        #     speak('Waiting for new command.')
        query = take_command().lower()

        if 'goodbye' in query: 
            speak("Goodbye sir! Talk to you next time.")
            sys.exit(0)
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            wquery = query.replace("wikipedia", "")
            wquery = wquery.replace("according to", "").strip()
            try:
                results = wikipedia.summary(wquery, sentences=2)
            except wikipedia.PageError:
                speak('No results found. Sorry sir!')
            else:
                speak("According to Wikipedia")
                print(results)
                speak(results)

        elif 'open youtube' in query:
           webbrowser.open("youtube.com") 

        elif 'open google' in query:
           webbrowser.open("google.com")

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")

        elif any([word in query for word in ['play music', 'next song', 'previous song','play song']]):
            play_music()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'email to sister' in query:
            try:
                speak("What should i say?")
                content = take_command()
                to = "stanislav.sabev@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")

        elif 'translate' in query:
            query = str(query).replace('translate', '').strip()
            result = trans(query)
            if not result:
                continue
            print(result)
            speak(result)

        i += 1