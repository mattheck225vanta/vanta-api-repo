import os
import requests
import json
from dotenv import load_dotenv

auth_url = "https://api.vanta.com/oauth/token"
load_dotenv()

def get_access_token():
  payload = json.dumps({
  "client_id": os.environ.get("MANAGE_VANTA_CLIENT_ID"),
  "client_secret": os.environ.get("MANAGE_VANTA_CLIENT_SECRET"),
  "scope": "vanta-api.all:read vanta-api.all:write",
  "grant_type": "client_credentials"
  })

  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", auth_url, headers=headers, data=payload)
  access_token = response.json()["access_token"]
  return access_token




