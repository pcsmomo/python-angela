#Data Types

#String
print("Hello"[0])
print("123" + "345")

#Integer
print(123 + 345)

# Python ignores underscore in Integer
print(123_456_789)

#Flaot
3.14159

#Boolean
False
True

# print("Your age is " + 20)
print("Your age is " + str(20))

print("my name")
print(type(20))

print(70 + float("100.5"))
print(str(70) + str(100))


print(type(6/3)) # float
print(2 ** 3) # This built-in exponent oprator ** is one of the reason 


# round(), float and int
print(round(2.6666666, 2))
print(8 // 3)
print(type(8 // 3))
print(4 / 2)
print(type(4 / 2))

result = 4 / 2
result /= 2
print(result)


# f-String
score = 0
height = 1.8
isWinning = True
print("your score is " + str(score) + ", your height is " + str(height) + "your are winning is " + str(isWinning))
# f-String
print(f"your score is {score}, your height is {height}, your are winning is {isWinning}")