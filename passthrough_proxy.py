from flask import Flask
from flask import Response
from flask import stream_with_context

import requests

app = Flask(__name__)

#Hosted path is constant and will change based on machine where ovirt engine is hosted
HOSTED_PATH = 'http://172.30.37.23/ovirt-engine/api'

#@app.route('/<url>')
def home(url):
    #
    url = HOSTED_PATH + url
    req = requests.get(url, stream = True)
    return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])


@app.route('/<url>')
def home(url):
    #print url
    requrl = "%s/%s/" %(HOSTED_PATH  ,url)
    print requrl
    session = requests.session()
    session.auth = ('admin@internal', 'password')
    request = getattr(session, 'get')
    response  = request(requrl, verify=False)
    return response


if __name__ == '__main__':
    app.run()
