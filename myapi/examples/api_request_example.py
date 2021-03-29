import requests
import io
import pickle

file = open(r'C:\Users\Roy\djangoProjects\djangoApi\myapi\examples\api_request_example.ps1', "wb+")
pickled_obj = pickle.dumps("Asd")

payload = {'name': "mynewmodel", 'model': pickled_obj}
payload = {
    "name": "proj_z",
    "mlmodels": [{"name": "model_z"}]
}
auth = ('roy', '1234')
url = "http://localhost:8000/api/mlproject/"

r = requests.post(url=url, json=payload, auth=auth)

print(r.status_code)
