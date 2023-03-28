sandwich_orders = ['pastrami', 'reuben',
                   'rachel', 'tuna salad', 'grilled cheese']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich} sandwich.")
print("Sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")
