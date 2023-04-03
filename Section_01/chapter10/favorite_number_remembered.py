from pathlib import Path
import json


def get_new_favorite_number(path):
    """Prompts user for favorite number"""
    number = input("Enter your favorite number: ")
    contents = json.dumps(number)
    path.write_text(contents)
    return number


def get_stored_favorite_number(path):
    """retrieves stored favorite number"""
    contents = path.read_text()
    number = json.loads(contents)
    return number


def favorite_number():
    path = Path('favorite_number.json')
    if path.exists():
        number = get_stored_favorite_number(path)
        print(f"I know your favorite number! It's {number}")
    else:
        number = get_new_favorite_number(path)
        print(
            f"Thanks for letting me know your favorite number is {number}. I'll remember it for next time.")


favorite_number()
