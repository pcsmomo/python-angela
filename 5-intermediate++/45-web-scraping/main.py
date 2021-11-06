from bs4 import BeautifulSoup
# import lxml
# if "html.parser" cannot parse properly, lxml provide a string parsing feature

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.name)    # tag name
# print(soup.title.string)  # content
# print(soup.prettify())    # prettified code
# print(soup.li)            # first li found
