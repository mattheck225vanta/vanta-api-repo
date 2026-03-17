import requests
from build_auth import get_access_token

url = "https://api.vanta.com/v1/resources/custom_resource"
access_token = get_access_token()

payload = {
    "resourceId": "699f4693feb3c4f41dd95cac",
    "resources": [
    {
        "displayName": "On-Prem DB Prod",
        "uniqueId": "onpremdbprod2468",
        "externalUrl": "https://mymonitor.MattDB.com",
        "customProperties": {
            "backupRetentionPeriodDays": 30,
            "dbClusterIdentifier": "mattdb-prod-cluster-01",
            "dbInstanceIdentifier": "mattdb-prod-instance-01",
            "dbInstanceStatus": True,
            "engine": "mysql",
            "name": "MattDB Production Primary",
            "publiclyAccessible": True,
            "storageEncrypted": True
            }
    },
    {
        "displayName": "On-Prem DB UAT",
        "uniqueId": "onpremdbuat2468",
        "externalUrl": "https://mymonitor.MattDB.com",
        "customProperties": {
            "backupRetentionPeriodDays": 30,
            "dbClusterIdentifier": "mattdb-uat-cluster-01",
            "dbInstanceIdentifier": "mattdb-uat-instance-01",
            "dbInstanceStatus": True,
            "engine": "mysql",
            "name": "MattDB UAT Primary",
            "publiclyAccessible": False,
            "storageEncrypted": False
            }
    },
    {
        "displayName": "On-Prem DB Dev",
        "uniqueId": "onpremdbdev2468",
        "externalUrl": "https://mymonitor.MattDB.com",
        "customProperties": {
            "backupRetentionPeriodDays": 30,
            "dbClusterIdentifier": "mattdb-dev-cluster-01",
            "dbInstanceIdentifier": "mattdb-dev-instance-01",
            "dbInstanceStatus": True,
            "engine": "mysql",
            "name": "MattDB Dev Primary",
            "publiclyAccessible": False,
            "storageEncrypted": True
            }
    }
]
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f'Bearer {access_token}'
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)