# List Comprehension

# Array
numbers = [1, 2, 3]
new_numbers = [n * n for n in numbers]
print(new_numbers)

# String
name = "Angela"
letter_list = [f"{letter}{letter}" for letter in name]
print(letter_list)

# Range
range_list = [num * 2 for num in range(1, 5)]
print(range_list)

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
