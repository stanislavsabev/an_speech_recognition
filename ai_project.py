import sys
import datetime
import time

import siri
import commands


tasks = {
    'wikipedia': commands.search_wikipedia,
    'open youtube': commands.open_youtube,
    'open google': commands.open_google,
    'open spotify': commands.open_spotify,
    'play music': commands.music_player,
    'next song': commands.music_player,
    'previous song': commands.music_player,
    'play song': commands.music_player,
    'the time': commands.the_time,
    'email to sister': commands.email_sister,
    'translate': commands.translator_handler,
    'open calendar': commands.open_calendar,
    'go to sleep': commands.go_to_sleep_siri,
}


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        siri.speak("Good Morning!")

    elif hour>=12 and hour<18:
        siri.speak("Good Afternoon!")

    else:
        siri.speak("Good Evening!")

    siri.speak("Sir, how can I help you?")


def main():
    wishMe()

    while True:
        query = siri.take_command().lower()
        if 'goodbye' in query: 
            siri.speak("Goodbye sir! Talk to you next time.")
            sys.exit(0)

        if siri.Siri.is_quiet:
            if 'hey siri' in query:
                commands.hey_siri(query)
            else:
                print('Sleeping...')
                time.sleep(2)
        else:
            # Logic for executing tasks based on query
            for command, task in tasks.items():
                if command in query:
                    task(query)
                    break
            else:
                print('Unknown command, try again!')


if __name__ == "__main__":
    main()