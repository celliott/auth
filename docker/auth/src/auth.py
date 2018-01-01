#!/usr/bin/env python

import os
import json
import requests
import logging
from flask import Flask, jsonify, request, Response
from functools import wraps

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

port = os.getenv('PORT', 3000)
debug = os.getenv('DEBUG', False)
vault_addr = os.getenv('VAULT_ADDR', 'http://127.0.0.1:8200')

app = Flask(__name__)

def check_auth(username, password):
  headers = {'content-type': 'application/json'}
  url = "{0}/v1/auth/userpass/login/{1}".format(vault_addr, username)
  data = json.dumps({ "password": password })
  r = requests.post(url, headers=headers, data=data)
  response = json.loads(r.text)
  try:
    if response['auth']['client_token']:
      logger.info("{} has been authenticated".format(username))
      return True
  except:
    pass

def authenticate():
  return Response(
  json.dumps({'authenticated': False}), 401,
  {'WWW-Authenticate': 'Basic realm="Login Required"'})

def auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
      return authenticate()
    return f(*args, **kwargs)
  return decorated

@app.route('/healthz', methods=['GET'])
def healthz():
  return json.dumps({'status':'ok'}), 200, {'ContentType':'application/json'}

@app.route('/', methods=['GET'])
@auth
def index():
  auth = request.authorization
  return json.dumps({ "authenticated": True, "user": auth.username })

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=port, debug=debug)
