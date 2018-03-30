import requests
import json
import logging as log


'''Set up the URL, payload, and header
   And then make the login post call
'''
url = 'http://35.193.187.38:8080/api/login'
payload = {"email":"shafeek@moogilu.com", "password":"123"}
headers = {'Content-Type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)
data = r.json()
tkn = ""   # API token


# Save the token for future calls to API
for key in data:
    if key == 'data':     # this data block holds user specific data
        tk = data[key]    # get the entire data block
        for ky in tk:
            if ky == 'token': # parse the data block for token
                tkn = tk[ky] # save the token for future API Calls
        print("token ="+ tkn)
