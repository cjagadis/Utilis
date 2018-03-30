import requests
import json

url = 'http://35.193.187.38:8080/api/login'
url2 = 'http://35.193.187.38:8080/'
# payload = {'key1': 'value1', 'key2': 'value2'}

payload = {"email":"shafeek@moogilu.com", "password":"123"}
headers = {'Content-Type': 'application/json'}
# GET
r = requests.get(url)

# GET with params in URL
#r = requests.get(url, params=payload)

# POST with form-encoded data
#r = requests.post(url, data=payload)

# POST with JSON 
import json
r = requests.post(url, data=json.dumps(payload), headers=headers)

# Response, status etc
print(r.text)
print(r.status_code)

r = requests.get(url2,params=payload)
# Response, status etc
print(r.text)
print(r.status_code)

