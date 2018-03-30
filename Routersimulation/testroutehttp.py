import requests
import json
import re

'''Simulating routing agent
   The router has received the forwarded request
   The HTTP/LB is simulated by testroute.py using
   Sanic acting as Asynchronous HTTP Server
'''


# GET
url3 = 'http://104.198.252.0:8000/'
r = requests.get(url3).json()
print(r)

# GET
url3 = 'http://104.198.252.0:8000/rtmp'
r = requests.get(url3)
data = r.json()
print(data)

if '200' in str(r): 
    print("success")

