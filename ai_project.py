import sys
import datetime
import time

import siri
import commands


tasks = {
    "wikipedia": commands.search_wikipedia,
    "open google": commands.open_google,
    "open spotify": commands.open_spotify,
    "play music": commands.music_player,
    "next song": commands.music_player,
    "previous song": commands.music_player,
    "play song": commands.music_player,
    "the time": commands.the_time,
    "email to sister": commands.email_sister,
    "translate": commands.translator_handler,
    "open calendar": commands.open_calendar,
    "go to sleep": commands.go_to_sleep_siri,
    "create folder": commands.create_folder,
    "youtube search": commands.youtube,
}


def show_commands(query):
    del query
    siri.speak("Showing commands!")
    print_commands()

def print_commands():
    commands_list = ", ".join(
        f"[{x}]" for x in list(tasks) + ["show commands", "goodbye"]
    )
    print("Commands: ")
    print(commands_list)


def wish_me():
    hour = datetime.datetime.now().hour
    greeting = ""
    if 0 <= hour < 12:
        greeting = "Good Morning!"

    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    siri.speak(f"{greeting} Sir, how can I help you?")


def main():
    wish_me()

    while True:
        query = siri.take_command().lower()
        if not query:
            print_commands()
            continue

        if "goodbye" in query:
            siri.speak("Goodbye sir! Talk to you next time.")
            sys.exit(0)

        if siri.Siri.is_quiet:
            if any(x in query for x in ["hey siri", "hey city"]):
                commands.hey_siri(query)
            else:
                print("Sleeping...")
                time.sleep(2)
        if "show commands" in query:
            show_commands(query)
        else:
            # Logic for executing tasks based on qu6ery
            for command, task in tasks.items():
                if command in query:
                    task(query)
                else:
                    print("Unknown command, try again!")


if __name__ == "__main__":
    main()


