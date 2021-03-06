# Python Summary Part 2

100 Days of Code - The Complete Python Pro Bootcamp for 2021 by Dr. Angela Yu

> File name prefix
> prefix x- : [Interactive Coding Exercise] \
> prefix z- : [Project]

# Details

## 4. Web Foundation

<details open>
  <summary>Click to Contract/Expend</summary>

## Section 41: Day 41 - Web Foundation - Introduction to HTML

### 347. How Does the Internet Actually Work?

[Submarine Cable Map](https://www.submarinecablemap.com/)

### 348. How Do Websites Actually Work?

[Techcrunch - Tech News](https://techcrunch.com/)

### 351. The Anatomy of an HTML Tag

[devdocs.io](https://devdocs.io/)

### 352. What we're building - HTML Personal Site

[Internet Achieve](https://archive.org/web/)

### 353. What is The HTML Boilerplate?

[Unicode Table](https://unicode-table.com/en/)

## Section 42: Day 42 - Web Foundation - Intermediate HTML

### 359. HTML Tables

[Interactive Resume - Pascal van Gemert](https://www.pascalvangemert.nl/)

## Section 43: Day 43 - Web Foundation - Introduction to CSS

### 369. Inline CSS

- [Well made Portfolio - Sean Designer](https://www.seanhalpin.design/)
- [Colour Palettes](https://colorhunt.co/)
- [Color - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value)

### 371. Internal CSS

Many tags are just boxes like <hr />

- [CSS Default Values Reference](https://www.w3schools.com/cssref/css_default_values.asp)
- [CSS border-style - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/border-style)

## Section 44: Day 44 - Web Foundation - Intermediate CSS

### 379. What Are Favicons?

[Favion.CC](https://www.favicon.cc/)

### 387. Adding Content to Our Website

- [Lorem Ipsum Generator](https://loremipsum.io/)
- [Flat Icon - Free Ventor Icons](https://www.flaticon.com/)
- [GIPHY - GIFs](https://giphy.com/)

## Section 45: Day 45 - Intermediate+ Web Scraping with Beautiful Soup

### 398. Parsing HTML and Making Soup

- [bs4 - Beautiful Soup Lib - Parse HTML file](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [pip bs4 install](https://pypi.org/project/beautifulsoup4/)
- [pip lxml - parser](https://pypi.org/project/lxml/)

### 401. Is Web Scraping Legal?

[reCAPCHA](https://www.google.com/recaptcha/about/)

- It prevents web scraping

- https://news.ycombinator.com/robots.txt
- https://edition.cnn.com/robots.txt
- https://www.linkedin.com/robots.txt
- Many web site actually declare what's allowed or not

## Section 46: Day 46 - Intermediate+ Create a Spotify Playlist using the Musical Time Machine

- [Billboard The Hot 100: 2013-12-31](https://www.billboard.com/charts/hot-100/2013-12-31/)
- [Spotify for developers](https://developer.spotify.com/dashboard/)
- [Spotify Documentation](https://spotipy.readthedocs.io/en/2.19.0/)
- [Spotify Documentation - URI list](https://spotipy.readthedocs.io/en/2.13.0/#ids-uris-and-urls)

## Section 47: Day 47 - Intermediate+ Create an Automated Amazon Price Tracker

> This would be useful!

- [CamelCamelCamel - Amazon Price History](https://camelcamelcamel.com/)
- [MY HTTP HEADER](http://myhttpheader.com/)

```py
# Stronger html parser
import lxml
soup = BeautifulSoup(response.content, "lxml")
```

### 413. How to Find and Select Elements on a Website with Selenium

- [find_element - Selenium-Python](https://selenium-python.readthedocs.io/locating-elements.html)
- [XPath - W3Schools](https://www.w3schools.com/xml/xpath_intro.asp)
  - chrome devTool -> mouse right click on an element -> Copy -> Copy XPath

### 417. The Cookie Clicker Project

- [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/)
- [Cookie Clicker Classic version](https://orteil.dashnet.org/experiments/cookie/)

## Section 54: Day 54 - Intermediate+ Introduction to Web Development with Flask

### 444. Understanding Backend Web Development with Python

- Flask: Comparably smaller project
- Django: Larger commercial project

### 445. Create your First Web Server with Flask

- [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- [pypi flask](https://pypi.org/project/Flask/)

```sh
export FLASK_APP=hello.py
/5-intermediate++/54-flask % . ../../venv/bin/activate
flask run
# Running on http://127.0.0.1:5000/
```

### 446. Understand the Command Line on Windows and Mac

[Terminal Mac Cheatsheet](https://github.com/appbrewery/terminal-mac-cheatsheet)

</details>
