import requests
import io
import pickle

file = io.StringIO()
pickled_obj = pickle.dumps("Asd")

payload = {'name': "mynewmodel", 'model': pickled_obj}
auth = ('roy', '1234')
url = "http://localhost:8000/api/models/"
r = requests.post(url=url, data=payload, auth=auth, files={'file':file})

print(r.status_code)
