import pickle

import requests

auth = ('roy', '1234')
url = r'http://localhost:8000/api/mlmodels/7/'

r = requests.get(url=url, auth=auth)

data =r.json()

file_url = data["upload"]

r = requests.get(url =file_url)

filecontent = r.content

obj = pickle.loads(filecontent)

print(obj)
