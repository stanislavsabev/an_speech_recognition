import os

song_number = 0
music_dir = 'songsforai'
songs = os.listdir(music_dir) 


def play_music(query):
    global song_number
    if 'previous song' in query:
        song_number -= 1
    elif 'next song' in query:
        song_number += 1
    print(songs[song_number])
    os.startfile(os.path.join(music_dir, songs[song_number]))