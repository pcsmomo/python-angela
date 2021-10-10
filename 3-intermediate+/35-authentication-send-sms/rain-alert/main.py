import requests
from twilio.rest import Client

# Open Weather Map
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "<API KEY>"

# Twilio SMS
account_sid = "TWILIO_ACCOUNT_SID"
auth_token = "TWILIO_AUTH_TOKEN"

# Melbourne
MY_LAT = -37.8136
MY_LONG = 144.9631
# MY_LAT = -37.17
# MY_LONG = 156.22


weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
# print(response.status_code)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+12345678901',
        to='+61123456789'
    )
    print(message.sid)
    print(message.status)
