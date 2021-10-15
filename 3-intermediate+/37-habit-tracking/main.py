import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "dkowiclasqjciasdfioeiraslkj",
    "username": "noahkim",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create my account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
