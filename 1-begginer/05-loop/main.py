#For Loop
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(f"{fruit} Pie")
print("Outside Looop")
# Indentation is very important

#For Loop with Range(start, end:exclude, step)
for number in range(1, 11, 3):
  print(number)

total = 0
for number in range(1, 101):
  total += number
print(total)