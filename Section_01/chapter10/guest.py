from pathlib import Path

name = input("Please enter your name: ")

path = Path('guests.txt')

path.write_text(name)
