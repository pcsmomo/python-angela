with open("x-data-overlap-text1.txt") as file1:
    list1 = file1.readlines()

with open("x-data-overlap-text2.txt") as file2:
    list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]

# Write your code above 👆
print(result)
