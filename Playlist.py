# playlist.py

# Khai báo danh sách toàn cục
songs = []

def show_menu():
    print("=== Music Playlist ===")
    print("1. Thêm bài hát")
    print("2. Xem danh sách bài hát")
    print("0. Thoát")

def main():
    while True:
        show_menu()
        choice = input("Chọn chức năng: ").strip()
        if choice == "1":
            print("Chức năng 'Thêm bài hát' sẽ được thêm sau.")
        elif choice == "2":
            print("Danh sách bài hát hiện đang trống.")
        elif choice == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
