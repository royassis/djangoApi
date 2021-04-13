import requests

url = "http://localhost:8000/api/mlproject/"
auth = ('roy', '1234')

r = requests.get(url=url, auth=auth)
project_id = int(r.json()[0].get("id"))

file = open(r'C:\Users\Roy\djangoProjects\djangoApi\myapi\scripts_requests\api_request.py', "rb")
files = {"upload": file}
payload = {'project': project_id, 'name': "model_new"}
url = "http://localhost:8000/api/mlmodels/"

r = requests.post(url=url, data=payload, auth=auth, files=files)

print(r.status_code)

file.close()
