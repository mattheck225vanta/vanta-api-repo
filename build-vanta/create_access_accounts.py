import requests
from build_auth import get_access_token

url = "https://api.vanta.com/v1/resources/user_account"
access_token = get_access_token()

payload = {
    "resources": [
        {
            "permissionLevel": "ADMIN",
            "status": "ACTIVE",
            "mfaEnabled": True,
            "mfaMethods": ["SMS"],
            "authMethod": "SSO",
            "displayName": "Matt Hecker UserAccess Test",
            "uniqueId": "123",
            "externalUrl": "www.matthecker.com",
            "fullName": "Matthew Hecker",
            "accountName": "MattHecker",
            "email": "matthew.hecker@realcompany.com",
            "createdTimestamp": "2026-02-01T14:52:09Z"
        },
                {
            "permissionLevel": "EDITOR",
            "status": "ACTIVE",
            "mfaEnabled": False,
            "mfaMethods": ["SMS"],
            "authMethod": "SSO",
            "displayName": "Ginny GRC UserAccess Test",
            "uniqueId": "456",
            "externalUrl": "www.ginnygrc.com",
            "fullName": "Ginny GRC",
            "accountName": "GinnyGRC",
            "email": "ginny.grc@realcompany.com",
            "createdTimestamp": "2026-02-02T14:52:09Z"
        },
                {
            "permissionLevel": "ADMIN",
            "status": "ACTIVE",
            "mfaEnabled": True,
            "mfaMethods": ["SMS"],
            "authMethod": "SSO",
            "displayName": "Build App Service Account",
            "uniqueId": "125",
            "externalUrl": "www.matthecker.com",
            "fullName": "Service Account",
            "accountName": "Service Account",
            "email": "serviceaccount@realcompany.com",
            "createdTimestamp": "2026-02-01T14:52:09Z"
        }
    ],
    "resourceId": "6924b2d2cdb83d7c327d3a02"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f'Bearer {access_token}'
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)