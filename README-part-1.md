# Python Summary Part 1

100 Days of Code - The Complete Python Pro Bootcamp for 2021 by Dr. Angela Yu

> File name prefix
> prefix x- : [Interactive Coding Exercise] \
> prefix z- : [Project]

# Details

## 1. Beginner

<details open>
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

## 2. Intermediate

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

### 145. Constructing Objects and Accessing their Attributes and Methods

[turtle](https://docs.python.org/3/library/turtle.html)

[turtle color](https://cs111.wellesley.edu/labs/lab01/colors)

### 147. Practice Modifying Object Attributes and Calling Methods

[Pypi - search python package](https://pypi.org/)\
[package - prettytable](https://pypi.org/project/prettytable/)\
[prettytable - doc](https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki)\
[Pokemon Pokedex](https://pokemondb.net/pokedex/game/x-y)

#### Using python package

```sh
# setup venv
python3 -m venv venv

# install new package, prettytable
. venv/bin/activate
(venv) python3 -m pip install prettytable
deactivate

# run python code with the environment installed new packages
venv/bin/python [python file path]
```

### 152. How to create your own Class in Python

- PascalCase
- camelCase
- snake_case

### 160. The Benefits of OOP: Use Open Trivia DB to Get New Questions

[Open Trivia Quiz Database](https://opentdb.com/)

### 163. Understanding Turtle Graphics and How to use the Documentation

[tkinter — Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html#module-tkinter)

### 169. Python Tuples and How to Generate Random RGB Colours

[Tuple : constant list](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

### 225. Reading CSV Data in Python

[Pandas - Data Analysis Library](https://pandas.pydata.org/)

[Pandas Documents](https://pandas.pydata.org/docs/index.html)

### 226. DataFrames & Series: Working with Rows & Columns

> Wow.... Python is getting more interesting

### 232. How to Create Lists using List Comprehension

List Comprehension is like Array.map in javascript

```py
new_numbers = [n * n for n in numbers]
```

### 245. Creating Windows and Labels with Tkinter

[tkinter - the Packer Document](https://docs.python.org/3/library/tkinter.html#the-packer)

### 248. \*\*kwargs: Many Keyword Arguments

```py
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        # colour and seats are optional
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")
```

### 254. How to work with the Canvas Widget and Add Images to Tkinter

[Color Hunt - Color matching](https://colorhunt.co/)

### 261. Challenge 1 - Working with Images and Setting up the Canvas

[Canvas Tk Doc](https://tkdocs.com/tutorial/canvas.html)

### 264. Challenge 3 - Saving Data to File

with keyword close file automatically

### 266. Generate a Password & Copy it to the Clipboard

[pyperclip - clipboard](https://pypi.org/project/pyperclip/)

```sh
(venv) python3 -m pip install pyperclip
```

### 273. Write, read and update JSON data in the Password Manager

- Write: json.dump()
- Read: json.load()
- Update: json.update()

### 280. Solution & Walkthrough for Creating New Flash Cards

[pandas.DataFrame.to_dict](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html)

</details>

## 3. Intermediate +

<details open>
  <summary>Click to Contract/Expend</summary>

### 292. Run Your Python Code in the Cloud!

[Python Anywhere](https://www.pythonanywhere.com/)

1. Craet an account
2. Upload all files
3. Open bash console (test running)
   ```sh
   python3 main.py
   ```
4. Tasks -> Add scheduled task
   1. the time is UTC time
   2. command : python3 main.py

But Python Anywhere service has expiry date which is annoying.

#### setup crontab on my local to send birthday wish email

1. Copy all files in my dropbox folder
2. install python
   1. `brew update`
   2. `brew instal python`
3. `python3 -m pip install virtualenv`
4. go to the path and `python3 -m venv env`
5. `. env/bin/activate`
6. `pip install pandas`
7. crontab -e
8. `* 11 * * * cd /Users/momo/Dropbox/Dev/python-small-program/birthday-wisher/ && . env/bin/activate && python3 main.py`

### 295. API Endpoints and Making API Calls

[International Space Station Current Location](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)

[pypi requests](https://pypi.org/project/requests/)

```sh
python -m pip install requests
```

### 296. Working with Responses: HTTP Codes, Exceptions & JSON Data

- [HTTP Status Codes](https://httpstatuses.com/)
  - 1XX: Hold On
  - 2XX: Here You Go
  - 3XX: Go Away
  - 4XX: You Screwed Up
  - 5XX: I Screwed Up
- [Python Requests Module Documentation](https://docs.python-requests.org/en/latest/)
  - [Errors and Exceptions](https://docs.python-requests.org/en/latest/user/quickstart/#errors-and-exceptions)
- [Convert Lat Long to Address](https://www.latlong.net/Show-Latitude-Longitude.html)

### 297. Challenge - Build a Kanye Quotes App using the Kanye Rest API

[Kanye rest](https://kanye.rest/)

### 298. Understand API Parameters: Match Sunset Times with the Current Time

[Sunset and sunrise times API](https://sunrise-sunset.org/api)

### 300. Day 34 Goals: what you will make by the end of the day

[Open Trivia Database](https://opentdb.com/)

### 303. Unescaping HTML Entities

- [HTML Entities](https://www.w3schools.com/html/html_entities.asp)
- [Formatter - HTML Escape/Unescape](https://www.freeformatter.com/html-escape.html)

### 311. Using API Keys to Authenticate and Get the Weather from OpenWeatherMap

- [Open Weather Map API](https://openweathermap.org/)
- [OWM - Current Weather Data](https://openweathermap.org/current)
- [OWM - One Call API](https://openweathermap.org/api/one-call-api)
- [OWM - My API Key](https://home.openweathermap.org/api_keys)

- [Latitude Longitude Finder](https://www.latlong.net/)
- [JSON Viewer](http://jsonviewer.stack.hu/)

### 312. Challenge - Check if it Will Rain in the Next 12 Hours

- [OWM - Weather Condition Code](https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2)

- [Ventusky Weather Map](https://www.ventusky.com/?p=-38.2;147.8;5&l=rain-3h)

### 313. Sending SMS via the Twilio API

[Twilio SMS Python Quickstart Document](https://www.twilio.com/docs/sms/quickstart/python)

```sh
# To run python3 in the vertual environment
venv/bin/python3 [relative path]
venv/bin/python3 2-intermediate/16-OOP/main.py
```

### 314. Use PythonAnywhere to Automate the Python Script

#### setup crontab on my local to send birthday wish email

1. Copy all files in my dropbox folder
2. install python
   1. `brew update`
   2. `brew instal python`
3. `python3 -m pip install virtualenv`
4. go to the path and `python3 -m venv env`
5. `. env/bin/activate`
6. `pip install twilio`
7. crontab -e
8. `* 07 * * * cd /Users/momo/Dropbox/Dev/python-small-program/rain-alert/ && . env/bin/activate && python3 main.py`

### 315. Understanding Environment Variables and Hiding API Keys

```sh
export OWM_API_KEY=
export TWILIO_ACCOUNT_SID=
export TWILIO_AUTH_TOKEN=
```

[List of APIs](https://apilist.fun/)

## Section 36: Day 36 - Intermediate+ Stock Trading News Alert Project

### 316. Day 36 Goals: what you will make by the end of the day

- [TSLA Stock Price](https://www.tradingview.com/symbols/NASDAQ-TSLA/)
- [Alpha Vantage API - Stock Price API](https://www.alphavantage.co/documentation/#daily)
- [News API](https://newsapi.org/)
- [Twilio API](https://www.twilio.com/)

## Section 37: Day 37 - Intermediate+ Habit Tracking Project: API Post Requests & Headers

### 322. HTTP Post Requests

- [Pixela API](https://pixe.la/)
- [Pixela API - Document](https://docs.pixe.la/)

### 323. Advanced Authentication using an HTTP Header

My Graph : https://pixe.la/v1/users/noahkim/graphs/graph1.html

### 324. Challenge: Add a Pixel to the Habit Tracker using a Post Request

[Pixela API - Post a Pixel](https://pixela-docs.hatenablog.com/entry/post-pixel)

### 325. Autofilling today's date using strftime

[Python Datetime - W3Schools](https://www.w3schools.com/python/python_datetime.asp)

## Section 38: Day 38 - Intermediate+ Workout Tracking Using Google Sheets

## 327. Day 38 Goals: what you will make by the end of the day

[OpenAI API](https://openai.com/blog/openai-api/)

- Python DateTime strftime()
- APIs and making POST requests
- Authorization Headers
- Environment Variables

- [Nutritionix API](https://www.nutritionix.com/business/api)
- [Nutritionix API - DOC](https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/preview)
- [Sheety API](https://sheety.co/)

## Section 39: Day 39 - Intermediate+ Capstone Part 1: Flight Deal Finder

## Section 40: Day 40 - Intermediate+ Capstone Part 2: Flight Club

</details>
