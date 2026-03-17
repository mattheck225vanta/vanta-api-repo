import requests
from manage_auth import get_access_token

url = "https://api.vanta.com/v1/documents"
access_token = get_access_token()

payload = {
    "title": "TEST API DOC",
    "description": "This is a test from the Manage Vanta API",
    "timeSensitivity": "MOST_RECENT",
    "cadence": "P0D",
    "reminderWindow": "P0D",
    "isSensitive": False
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f'Bearer {access_token}'
}

response = requests.post(url, json=payload, headers=headers)
