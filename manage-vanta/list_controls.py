import requests
from manage_auth import get_access_token

access_token = get_access_token()

url = "https://api.vanta.com/v1/controls?pageSize=10"

headers = {
    "accept": "application/json",
    "authorization": f'Bearer {access_token}'
}

response = requests.get(url, headers=headers)

# print(json.dumps(response))
print(response.text)