import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "<API KEY>"

# Melbourne
MY_LAT = -37.8136
MY_LONG = 144.9631

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key
}


response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.status_code)
print(response.json())
