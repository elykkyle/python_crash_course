from pathlib import Path

path = Path('cats.txt')
try:
    contents = path.read_text().rstrip()
except FileNotFoundError:
    print(f"File {path} not found.")
print(contents)
contents = ''
path = Path('dogs.txt')
try:
    contents = path.read_text().rstrip()
except FileNotFoundError:
    print(f"File {path} not found.")
print(contents)
