import datetime

from siri import speak, take_command 
import webbrowser
import music
import emails
import translate
import theday
import wikipedia


def search_wikipedia(query):
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


def open_youtube(query):
    webbrowser.open("youtube.com") 


def open_google(query):
    webbrowser.open("google.com")


def open_spotify(query):
    webbrowser.open("spotify.com")


def music_player(query):
    music.play_music(query)


def the_time(query):
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")


def email_sister():
    try:
        speak("What should i say?")
        content = take_command()
        to = "stanislav.sabev@gmail.com"
        emails.sendEmail(to, content)
        speak("Email has been sent")
    except Exception as e:
        print(e)
        speak("Sorry my friend . I am not able to send this email")


def translate(query):
    speak('What do you want to translate?')
    query = take_command()
    result = translate.trans(query)
    if result:
        speak('Showing translaton.')
        print(result)


def open_calendar():
    week_day = theday.weekday()
    if week_day is None:
        speak('Unknown date.')
    else:
        speak(f"You were born on {week_day}")

