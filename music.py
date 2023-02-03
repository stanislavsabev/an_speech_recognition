import os

song_number = 0
music_dir = "songsforai"


def play_music(query):
    global song_number

    songs = os.listdir(music_dir)

    if "previous song" in query:
        song_number -= 1
    elif "next song" in query:
        song_number += 1
    song_file = os.path.join(music_dir, songs[song_number])
    if not os.path.isfile(song_file):
        print(f"Missing song file {song_file}")
        return
    print(songs[song_number])
    os.startfile(song_file)
