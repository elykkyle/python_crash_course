from pathlib import Path

path = Path('cats.txt')
try:
    contents = path.read_text().rstrip()
except FileNotFoundError:
    pass
print(contents)
contents = ''
path = Path('dogs.txt')
try:
    contents = path.read_text().rstrip()
except FileNotFoundError:
    pass
print(contents)
