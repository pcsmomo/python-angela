from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# 2013-12-31

response = requests.get('https://www.billboard.com/charts/hot-100/' + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_h3s = soup.find_all("h3", class_="c-title")
song_names = [song.getText().strip() for song in song_names_h3s]
# print(song_names)

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="YOUR UNIQUE CLIENT ID",
        client_secret="YOUR UNIQUE CLIENT SECRET",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
# print(user_id)
