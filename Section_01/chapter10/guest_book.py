from pathlib import Path

path = Path('guest_book.txt')

guest_list = ''

while True:
    name = input("Please enter your name: ")
    guest_list += f"{name}\n"
    more = input("Input another name? (yes/no)")
    if more == 'no':
        break

path.write_text(guest_list)
