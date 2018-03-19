import requests
import json
import logging as log

args = p.parse_args()

if args.verbose:
    log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
    log.info("Verbose output.")
else:
    log.basicConfig(format="%(levelname)s: %(message)s")

log.info("This should be verbose.")
log.warning("This is a warning.")
log.error("This is an error.")


'''Set up the URL, payload, and header
   And then make the login post call
'''
url = 'http://35.193.187.38:8080/api/login'
payload = {"email":"shafeek@moogilu.com", "password":"123"}
headers = {'Content-Type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)
data = r.json()

log.info(data)
log.info(("status code = ") + str(r.status_code))

# Save the token for future calls to API
for key in data:
    if key == 'data':     # this data block holds user specific data
        tk = data[key]    # get the entire data block
        for ky in tk:
            if ky == 'token': # parse the data block for token
                tkn = tk[ky] # save the token for future API Calls
        log.info("token ="+ tkn)
