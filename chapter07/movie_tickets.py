prompt = "Enter your age to get your ticket price."
prompt += "\nEnter 'quit' to end."
prompt += "\nAge: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        price = 'free'
    elif age <= 12:
        price = '$10'
    elif age > 12:
        price = '$15'
    print(f"Your ticket is {price}.")
