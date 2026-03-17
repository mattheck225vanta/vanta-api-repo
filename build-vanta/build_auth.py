import os
import json
import requests
from dotenv import load_dotenv

auth_url = "https://api.vanta.com/oauth/token"
load_dotenv()

def get_access_token():
  payload = json.dumps({
  "client_id": os.environ.get("BUILD_VANTA_CLIENT_ID"),
  "client_secret": os.environ.get("BUILD_VANTA_CLIENT_SECRET"),
  "scope": "connectors.self:write-resource",
  "grant_type": "client_credentials"
  })

  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", auth_url, headers=headers, data=payload)
  # print(response.json())
  access_token = response.json()["access_token"]
  return access_token

