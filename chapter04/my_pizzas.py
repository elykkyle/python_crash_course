my_pizzas = ['veggie', 'supreme', 'polish']

friend_pizzas = my_pizzas[:]

my_pizzas.append('garlic')

friend_pizzas.append('mushroom')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)


print("My friends' favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
