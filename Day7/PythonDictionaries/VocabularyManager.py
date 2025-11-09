from colorama import init, Fore, Back, Style
import os
import time

# Khởi tạo colorama
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    width = 50
    print(Fore.CYAN + "╔" + "═" * (width-2) + "╗")
    print("║" + text.center(width-2) + "║")
    print("╚" + "═" * (width-2) + "╝" + Style.RESET_ALL)

def print_menu():
    clear_screen()
    print_header(" TỪ ĐIỂN ANH - VIỆT ")
    print(Fore.YELLOW + "\n┌─── MENU CHỨC NĂNG ───┐")
    print("│                      │")
    print(f"│  {Fore.GREEN}1.{Fore.WHITE} Thêm từ mới       {Fore.YELLOW}│")
    print(f"│  {Fore.GREEN}2.{Fore.WHITE} Tìm nghĩa của từ  {Fore.YELLOW}│")
    print(f"│  {Fore.GREEN}3.{Fore.WHITE} Cập nhật nghĩa    {Fore.YELLOW}│")
    print(f"│  {Fore.GREEN}4.{Fore.WHITE} Xóa từ            {Fore.YELLOW}│")
    print(f"│  {Fore.GREEN}5.{Fore.WHITE} Hiển thị từ điển  {Fore.YELLOW}│")
    print(f"│  {Fore.GREEN}6.{Fore.WHITE} Kiểm tra từ       {Fore.YELLOW}│")
    print(f"│  {Fore.GREEN}7.{Fore.WHITE} Thoát             {Fore.YELLOW}│")
    print("│                      │")
    print("└──────────────────────┘" + Style.RESET_ALL)

def add_word(dictionary):
    word = input("Nhập từ tiếng Anh: ").lower()
    if word in dictionary:
        print(f"Từ '{word}' đã tồn tại!")
        return
    meaning = input("Nhập nghĩa tiếng Việt: ")
    example = input("Nhập ví dụ (không bắt buộc): ")
    dictionary[word] = {
        "meaning": meaning,
        "example": example
    }
    print(f"Đã thêm từ '{word}' vào từ điển!")

def find_word(dictionary):
    word = input("Nhập từ cần tìm: ").lower()
    if word in dictionary:
        entry = dictionary[word]
        print(f"\nTừ: {word}")
        print(f"Nghĩa: {entry['meaning']}")
        if entry['example']:
            print(f"Ví dụ: {entry['example']}")
    else:
        print(f"Không tìm thấy từ '{word}'")

def update_word(dictionary):
    word = input("Nhập từ cần cập nhật: ").lower()
    if word in dictionary:
        new_meaning = input("Nhập nghĩa mới: ")
        new_example = input("Nhập ví dụ mới (không bắt buộc): ")
        dictionary[word] = {
            "meaning": new_meaning,
            "example": new_example
        }
        print(f"Đã cập nhật từ '{word}'!")
    else:
        print(f"Không tìm thấy từ '{word}'")

def delete_word(dictionary):
    word = input("Nhập từ cần xóa: ").lower()
    if word in dictionary:
        confirm = input(f"Bạn có chắc muốn xóa từ '{word}'? (y/n): ")
        if confirm.lower() == 'y':
            del dictionary[word]
            print(f"Đã xóa từ '{word}'")
    else:
        print(f"Không tìm thấy từ '{word}'")

def show_all_words(dictionary):
    if not dictionary:
        print("Từ điển trống!")
        return
    
    print("\n=== DANH SÁCH TỪ VỰNG ===")
    for word, entry in dictionary.items():
        print(f"\nTừ: {word}")
        print(f"Nghĩa: {entry['meaning']}")
        if entry['example']:
            print(f"Ví dụ: {entry['example']}")
    print("========================")

def practice_words(dictionary):
    if not dictionary:
        print("Từ điển trống!")
        return
    
    import random
    word = random.choice(list(dictionary.keys()))
    print(f"\nNghĩa của từ '{word}' là gì?")
    answer = input("Trả lời: ")
    
    if answer.lower() == dictionary[word]['meaning'].lower():
        print("Chính xác!")
    else:
        print(f"Sai rồi! Nghĩa đúng là: {dictionary[word]['meaning']}")

def main():
    vocabulary = {}
    while True:
        print_menu()
        choice = input("Chọn chức năng (1-7): ")
        
        if choice == '1':
            add_word(vocabulary)
        elif choice == '2':
            find_word(vocabulary)
        elif choice == '3':
            update_word(vocabulary)
        elif choice == '4':
            delete_word(vocabulary)
        elif choice == '5':
            show_all_words(vocabulary)
        elif choice == '6':
            practice_words(vocabulary)
        elif choice == '7':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()