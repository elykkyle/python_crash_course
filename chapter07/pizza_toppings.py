prompt = ("What topping would you like to add to your pizza?")
prompt += ("\nIf nothing more, enter 'quit' to end. ")

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza...")
