import datetime

import siri 
import webbrowser
import music
import emails
import translator
import theday
import wikipedia


def search_wikipedia(query):
    siri.speak('Searching Wikipedia...')
    wquery = query.replace("wikipedia", "")
    wquery = wquery.replace("according to", "").strip()
    try:
        results = wikipedia.summary(wquery, sentences=2)
    except wikipedia.PageError:
        siri.speak('No results found. Sorry sir!')
    else:
        siri.speak("According to Wikipedia")
        print(results)
        siri.speak(results)


def open_youtube(query):
    del query
    webbrowser.open("youtube.com") 


def open_google(query):
    del query
    webbrowser.open("google.com")


def open_spotify(query):
    del query
    webbrowser.open("spotify.com")


def music_player(query):
    music.play_music(query)


def the_time(query):
    del query
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    siri.speak(f"Sir, the time is {strTime}")


def email_sister(query):
    del query
    try:
        siri.speak("What should i say?")
        content = siri.take_command()
        to = "stanislav.sabev@gmail.com"
        emails.sendEmail(to, content)
        siri.speak("Email has been sent")
    except Exception as e:
        print(e)
        siri.speak("Sorry my friend . I am not able to send this email")


def translator_handler(query):
    del query
    result = translator.translate()
    if result:
        siri.speak('Showing translasion.')
        print(result)


def open_calendar(query):
    del query
    week_day = theday.weekday()
    if week_day is None:
        siri.speak('Unknown date.')
    else:
        siri.speak(f"You were born on {week_day}")


def go_to_sleep_siri(query):
    del query
    siri.speak('Going to sleep.')
    siri.go_quiet(True)


def hey_siri(query):
    del query
    print('Siri waking up...')
    siri.speak('Hello again sir!')
    siri.go_quiet(False)