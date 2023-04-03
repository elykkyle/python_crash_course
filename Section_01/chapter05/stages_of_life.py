age = 10

if age < 2:
    message = "person is a baby"
elif age < 4:
    message = "person is a toddler."
elif age < 13:
    message = "person is a kid."
elif age < 20:
    message = "person is a teenager"
elif age < 65:
    message = "person is an adult"
elif age >= 65:
    message = "person is an elder"
print(message)
