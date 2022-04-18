import sys
import datetime

from siri import speak
from siri import take_command
import command_hendlers as ch

commands = {
    'wikipedia': ch.search_wikipedia,
    'open youtube': ch.open_youtube,
    'open google': ch.open_google,
    'open spotify': ch.open_spotify,
    'play music': ch.music_player,
    'next song': ch.music_player,
    'previous song': ch.music_player,
    'play song': ch.music_player,
    'the time': ch.the_time,
    'email to sister': ch.email_sister,
    'translate': ch.translate,
    'open calendar': ch.open_calendar,
}


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello Sir. how can I help you?")


if __name__ == "__main__":
    wishMe()
    i = 0
    while True:
        query = take_command().lower()

        if 'goodbye' in query: 
            speak("Goodbye sir! Talk to you next time.")
            sys.exit(0)
        
        # Logic for executing tasks based on query
        for command, handler in commands.items():
            if command in query:
                handler(query)
                break
        else:
            speak('Unknown command, try again!')
        i += 1