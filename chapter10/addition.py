
def addition():
    while True:
        num_1 = input("Enter the first number: ")
        try:
            num_1 = int(num_1)
            break
        except ValueError:
            print("That's not a valid number")
    while True:
        num_2 = input("Enter the second number: ")
        try:
            num_2 = int(num_2)
            break
        except ValueError:
            print("that's not a valid number")
    try:
        print(f"{num_1 + num_2}")
    except TypeError:
        print("Invalid input entered.")


addition()
