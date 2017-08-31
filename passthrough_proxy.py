from flask import Flask
from flask import Response
from flask import stream_with_context

import requests

app = Flask(__name__)

#Hosted path is constant and will change based on machine where ovirt engine is hosted
HOSTED_PATH = 'http://localhost:10000/'

@app.route('/<url>')
def home(url):
    #
    url = HOSTED_PATH + url
    req = requests.get(url, stream = True)
    return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])

if __name__ == '__main__':
    app.run()
