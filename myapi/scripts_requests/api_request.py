import requests
from pathlib import Path

# Get some project id from repo
url = "http://localhost:8000/api/mlproject/"
auth = ('roy', '1234')

r = requests.get(url=url, auth=auth)
project_id = int(r.json()[0].get("id"))

# Send request - create new model with file upload
p = Path(__file__).parent.joinpath("api_request.py")
file = open(p, "rb")
files = {"upload": file}
payload = {'project': project_id, 'name': "model_new"}
url = "http://localhost:8000/api/mlmodels/"

r = requests.post(url=url, data=payload, auth=auth, files=files)

print(r.status_code)

file.close()
