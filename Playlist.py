songs = []

def add_song(title, artist, duration):
    song = {
        "title": title,
        "artist": artist,
        "duration": duration
    }
    songs.append(song)
    return song

def view_playlist():
    if not songs:
        print("Playlist hiện đang trống.")
        return
        
    print("Danh sách bài hát trong playlist:")
    for index, song in enumerate(songs, start=1):
        print(f"{index}. {song['title']} - {song['artist']} ({song['duration']}s)")
        

# Test nhanh:
if __name__ == "__main__":
    add_song("Lạc Trôi", "Sơn Tùng MTP", 240)
    add_song("Nơi Này Có Anh", "Sơn Tùng MTP", 230)

    view_playlist()