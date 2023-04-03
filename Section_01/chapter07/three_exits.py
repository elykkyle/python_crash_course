prompt = ("What topping would you like to add to your pizza?")
prompt += ("\nIf nothing more, enter 'quit' to end. ")
prompt += ("\nTopping: ")

topping_count = 0

while topping_count <= 5:
    topping = input(prompt)
    if topping == 'quit':
        topping_count = 6
    topping_count += 1
    print(f"Adding {topping} to your pizza...")

active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza...")


while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza...")
