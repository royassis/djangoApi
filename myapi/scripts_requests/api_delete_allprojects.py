from concurrent.futures import ThreadPoolExecutor

import requests

auth = ('roy', '1234')
url = r'http://localhost:8000/api/mlproject/'

r = requests.get(url=url, auth=auth)

data =r.json()

with ThreadPoolExecutor() as executor:
    futures = [requests.delete(url+f"{mlproject['id']}/") for mlproject in data]


