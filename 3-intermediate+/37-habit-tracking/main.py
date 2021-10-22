import requests
from datetime import datetime

USERNAME = "noahkim"
TOKEN = "dkowiclasqjciasdfioeiraslkj"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Step 1. Create my account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# # {"message":"Success.","isSuccess":true}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "page",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Step 2. Create my graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# # {"message":"Success.","isSuccess":true}

# Step 3. Look at my Reading graph
# https://pixe.la/v1/users/noahkim/graphs/graph1.html

# Step 4. Post a pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# yesterday = datetime(year=2021, month=10, day=21)
# print(yesterday.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
