import pickle

import requests

auth = ('roy', '1234')
url = r'http://localhost:8000/api/mlproject/'

r = requests.get(url=url, auth=auth)

data =r.json()

for mlproject in data:
    print(mlproject)
    requests.delete(url+f"{mlproject['id']}/")

