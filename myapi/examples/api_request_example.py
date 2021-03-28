import requests
import io

file = io.StringIO()

payload = {'name': "as12d", 'model': "asd".encode("utf8")}
auth = ('roy', '1234')
url = "http://localhost:8000/api/models/"
r = requests.post(url=url, data=payload, auth=auth, files={'model':file})

print(r.status_code)
