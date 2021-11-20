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

print("\n== soup.find_all ==")
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

# <h1 id="name">
print("\n== soup.find ==")
heading = soup.find(name="h1", id="name")
print(heading)

# <h3 class="heading">
section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)   # tag name, h3
# print(section_heading.get("class"))
print(section_heading)

# CSS Selectors
print("\n== CSS Selectors ==")
company_url = soup.select_one(selector="p a")
print(company_url)
name = soup.select_one(selector="#name")
print(name)
headings = soup.select(selector=".heading")
print(headings)
