def make_sandwich(*toppings):
    print("Sandwich toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_sandwich('peanut butter', 'jelly')
make_sandwich('peanut butter', 'american cheese', 'honey')
make_sandwich('mushrooms', 'cheese', 'lettuce',
              'onion', 'tomato', 'mustard', 'avocado')
