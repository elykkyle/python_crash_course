from pathlib import Path
import json


def get_stored_user(path):
    """Get stored user if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None


def get_new_user(path):
    """Prompt for a new username."""
    new_user = {}
    new_user['username'] = input("What is your name? ")
    new_user['favorite_number'] = input("What is your favorite number? ")
    new_user['favorite_color'] = input("What is your favorite color? ")
    contents = json.dumps(new_user)
    path.write_text(contents)
    return new_user


def greet_user():
    """Greet the user by name."""
    path = Path('user.json')
    user = get_stored_user(path)
    if user:
        print(
            f"Welcome back, {user['username']}! I see your favorite number is {user['favorite_number']}, and your favorite color is {user['favorite_color']}.")
    else:
        user = get_new_user(path)
        print(f"We'll remember you when you come back, {user['username']}!")


greet_user()
