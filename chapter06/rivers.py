rivers = {
    'nile': 'egypt',
    'mississippi': 'united states of america',
    'amazon': 'brazil'
}

for k, v in rivers.items():
    print(f"The {k.title()} runs through {v.title()}")

for key in rivers:
    print(f"{key.title()}")
# OR:
# for key in rivers.keys():
#     print(f"{key.title()}")

for value in rivers.values():
    print(f"{value.title()}")
