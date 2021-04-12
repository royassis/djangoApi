import requests

file = open(r'C:\Users\Roy\djangoProjects\djangoApi\myapi\scripts_requests\api_get_list.py', "wb+")
files = {"file": file}

payload = {'project': 25, 'name': "model_i"}
auth = ('roy', '1234')
url = "http://localhost:8000/api/mlmodels/"

r = requests.post(url=url, data=payload, auth=auth, files=files)

print(r.status_code)

file.close()
