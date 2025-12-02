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

def search_by_artist(artist_name):
    results = [song for song in songs if song["artist"].lower() == artist_name.lower()]

    if not results:
        print(f"Không tìm thấy bài hát nào của ca sĩ: {artist_name}")
        return

    print(f"Các bài hát của '{artist_name}':")
    for index, song in enumerate(results, start=1):
        print(f"{index}. {song['title']} ({song['duration']}s)")


# Test nhanh:
if __name__ == "__main__":
    add_song("Lạc Trôi", "Sơn Tùng MTP", 240)
    add_song("Nơi Này Có Anh", "Sơn Tùng MTP", 230)
    add_song("Em Của Ngày Hôm Qua", "Sơn Tùng MTP", 215)
    add_song("Tháng Tư Là Lời Nói Dối Của Em", "Hà Anh Tuấn", 300)

    search_by_artist("Sơn Tùng MTP")