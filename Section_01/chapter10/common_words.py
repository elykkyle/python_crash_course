from pathlib import Path

filenames = ['moby_dick.txt', 'little_women.txt', 'alice.txt']

for file in filenames:
    path = Path(file)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"file {path} doesn't exist")
    count = contents.lower().count('the ')
    print(f"The word 'the' appears in {path} {count} times.")
