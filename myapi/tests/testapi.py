import requests

r = requests.post('http://localhost:8000/models/', data={'name': 'model1', 'model': b'asd'}, auth=('roy', '1234'))
print(r.text)
