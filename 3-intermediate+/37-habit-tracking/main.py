import requests

USERNAME = "noahkim"
TOKEN = "dkowiclasqjciasdfioeiraslkj"

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
    "id": "graph1",
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

# Step 3. https://pixe.la/v1/users/noahkim/graphs/graph1.html
