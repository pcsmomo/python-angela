from bs4 import BeautifulSoup
import requests

date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# 2013-12-31

response = requests.get('https://www.billboard.com/charts/hot-100/' + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_h3s = soup.find_all("h3", class_="c-title")
song_names = [song.getText().strip() for song in song_names_h3s]
print(song_names)
