sandwich_orders = ['pastrami', 'reuben', 'pastrami',
                   'rachel', 'tuna salad', 'pastrami', 'grilled cheese']
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich} sandwich.")
print("Sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")
