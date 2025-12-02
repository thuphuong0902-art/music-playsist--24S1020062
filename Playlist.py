songs = []

def add_song(title, artist, duration):
    song = {
        "title": title,
        "artist": artist,
        "duration": duration
    }
    songs.append(song)
    return song

# Ví dụ chạy thử
if __name__ == "__main__":
    t = input("Tên bài hát: ")
    a = input("Ca sĩ: ")
    d = int(input("Thời lượng (giây): "))
    
    added = add_song(t, a, d)
    print("Đã thêm:", added)