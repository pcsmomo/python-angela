# Python Summary

100 Days of Code - The Complete Python Pro Bootcamp for 2021 by Dr. Angela Yu

> File name prefix
> prefix x- : [Interactive Coding Exercise] \
> prefix z- : [Project]

# Details

## Beginner

<details>
  <summary>Click to Contract/Expend</summary>

### 17. Python Primitive Data Types

Python ignores underscore in Integer

```py
print(123_456_789)
# 123456789
```

### 18. Type Error, Type Checking and Type Conversion

Python is stricly checking types

```py
print("Your age is " + 20)
# TypeError: can only concatenate str (not "int") to str
```

### 20. Mathematical Operations in Python

```py
print(2 ** 3)
# 8
# This built-in exponent oprator ** is one of the reasons
# python is loved by data scientist and mathematicians
```

### 22. Number Manipulation and F Strings in Python

f-string

```py
score = 0
height = 1.8
isWinning = True
# this is pain in the axx
print("your score is " + str(score) + ", your height is " + str(height) + "your are winning is " + str(isWinning))

# f-String : formatted string literals
print(f"your score is {score}, your height is {height}, your are winning is {isWinning}")
```

### 24. Day 2 Project: Tip Calculator

```py
# 4 different ways to format to two decimal points
pi = 3.14159
print("%.2f" % pi)
print("%.2f" % round(pi, 2))
print("{:.2f}".format(pi))
print("{:.2f}".format(round(pi, 2)))
```

### 28. [Interactive Coding Exercise] Odd or Even? Introducing the Modulo

% : Mmodulo Oprator (Rest)

### 31. [Interactive Coding Exercise] Leap Year

Try to write flow chart first before implements

### 32. Multiple If Statements in Succession

Indentation in python is very important

### 36. Day 3 Project: Treasure Island

[ASCII ART](https://ascii.co.uk/art)

```py
# 3 single quotes
print('''
            __  __
           / _|/ _|
  ___ ___ | |_| |_ ___  ___
 / __/ _ \|  _|  _/ _ \/ _ \\
| (_| (_) | | | ||  __/  __/
 \___\___/|_| |_| \___|\___|
''')
```

### 39. Random Module

[Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister)

[Pseudorandom number generators](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators)

[AskPython Random Module](https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences)

</details>
