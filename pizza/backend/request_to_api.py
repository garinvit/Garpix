import requests
import json

data = {
    "pizza":
        {
            "name": "7 сыра",
            "description": "Пицца из смеси сыров",
            # "slug": "7-syra",
            "tags": [
                3,
                4]
        }
}
url = "http://127.0.0.1:8000/api/v1/pizzas/"
token = "20cbbd13b60fc0c5655a7b3e7c8bc7b507041074"
headers = {
    'authorization': f"Token {token}",
    'content-type': "application/json",
}

response = requests.request("POST", url, data=json.dumps(data), headers=headers)

print(response.text)