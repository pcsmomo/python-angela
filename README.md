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

### 47. Day 5 Goals: what we will make by the end of the day

[Check if you account hacked](https://haveibeenpwned.com/)

### 59. Indentation in Python

[Python Style Guide](https://www.python.org/dev/peps/pep-0008/#indentation)

### 118. Introducing the Final Project: The Number Guessing Game

[My Own ASCII Text](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)

[Python Tutor : Online Python Debugging Tool](http://pythontutor.com/)

</details>

## Intermediate

<details open>
  <summary>Click to Contract/Expend</summary>

### 140. Introduction & Requirements for the Coffee Machine Project

1. Using Todo List

```py
# TODO: 1. Print report of all coffee machine resource
# TODO: 2. Check resources sufficient to make drink order
```

2. [Searching Emoji](https://emojipedia.org/)
3. [Mac Emoji Shortcut](https://support.apple.com/en-gb/guide/mac-help/mchlp1560/mac) : Edit > Emoji & Symbols (Ctrl + Command + Space)
4. [Windows Emoji Shortcut](https://support.microsoft.com/en-gb/windows/windows-10-keyboard-tips-and-tricks-588e0b72-0fff-6d3f-aeee-6e5116097942) : Windows logo key + .(period)
5. [PyCharm keyoard shortcuts](https://www.jetbrains.com/help/pycharm/mastering-keyboard-shortcuts.html)

### 141. Solution & Walkthrough for the Coffee Machine Code

Multi Selection with a cursor

- VSCode, PyCharm: Option(Alt) + Shift + Drag mouse cursor
- Sublime : Option(Alt) + Drag mouse cursor

</details>
