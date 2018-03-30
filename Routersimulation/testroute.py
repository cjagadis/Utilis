from sanic import Sanic
from sanic.response import json

'''Simulation of LB HTTP Server
   It is done using Sanic package
   This does not work on Windows
   Testrouted.py is the agent that
   recieves request from the testforward.py
'''

app = Sanic()

@app.route('/')
async def test(reqest):
    return json({'hello': 'world'})

@app.route('/rtmp')
async def rtmp(requst):
    return json({'alloc': 'rtmp'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
