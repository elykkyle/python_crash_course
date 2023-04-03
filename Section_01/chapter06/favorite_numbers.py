favorite_numbers = {
    'john': 25,
    'april': 8,
    'david': 11,
    'patrice': 7,
    'ralph': 36
}

print(f"John's favorite number is {favorite_numbers.get('john', 'unknown')}")
print(f"April's favorite number is {favorite_numbers.get('april', 'unknown')}")
print(f"David's favorite number is {favorite_numbers.get('david', 'unknown')}")
print(
    f"Patrice's favorite number is {favorite_numbers.get('patrice', 'unknown')}")
print(f"Ralph's favorite number is {favorite_numbers.get('ralph', 'unknown')}")
print(f"Luke's favorite number is {favorite_numbers.get('luke', 'unknown')}")
