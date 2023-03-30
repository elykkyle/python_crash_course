from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text().strip()
print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)
