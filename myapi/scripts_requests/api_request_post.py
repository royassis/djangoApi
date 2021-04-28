import requests
from pathlib import Path

# Get some project id from repo
auth = ('roy', '1234')
payload = {'data': [[1,2,3,4]]}
url = "http://localhost:8000/api/mlproject/7/predict"

r = requests.post(url=url, json=payload, auth=auth)

print(r.status_code)

print(r.json())