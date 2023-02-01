from datetime import datetime
from urllib import response
import requests, json, base64;
import hashlib, hmac;

class Simpler:
  def __init__(self, server):
    self._server = server
    self._session = requests.Session()
    self._lastMessage = None
    self._lastContent = None
    self._lastResult = None
    self._endpoints = None

  def authenticate(self, credentials):
    credentials = credentials.split()
    return self._authenticate(credentials[0], credentials[1], credentials[2])

  def _authenticate(self, appId, authorization, password):
    succeeded = False
    authResponse = self._session.get(self._server + '/api/' + appId, params = {'_signature': authorization})
    if authResponse.status_code == 200:
      authJson = authResponse.json()
      nonce = str(int((datetime.utcnow() - datetime(1, 1, 1)).total_seconds() * 10**7))
      password = hmac.new(password.encode('utf-8'), digestmod = 'sha256')
      password.update((authJson['Nonce'] + nonce).encode('utf-8'))
      signInResponse = self._session.post(self._server + authJson['SignInUrl'], {'UserId': appId, 'Nonce': nonce, 'Password': base64.b64encode(password.digest()).decode('ASCII')})
      self._setLastMessage(signInResponse)
      if signInResponse.status_code == 200:
        self._endpoints = signInResponse.json()
        succeeded = True
    else:
      self._setLastMessage(authResponse)

    return succeeded

  def get(self, endpoint, data = None):
    return self._invoke('GET', endpoint, data)

  def _invoke(self, method, endpoint, data):
    self._lastMessage = None
    self._lastResult = None
    succeeded = False
    endpoint = method + ' ' + endpoint
    if endpoint in self._endpoints:
      if method == 'POST':
        response = self._session.post(self._server + self._endpoints[endpoint], json = data)
      elif method == 'PUT':
        response = self._session.put(self._server + self._endpoints[endpoint], json = data)
      elif method == 'GET':
        response = self._session.get(self._server + self._endpoints[endpoint], params = data)
      else:
        response = self._session.request(method, self._server + self._endpoints[endpoint], json = data)
      self._setLastMessage(response)
      if response.status_code == 200:
        self._setLastResult(response)
        succeeded = True
    else:
      print('Endpoint not found: ' + endpoint)

    return succeeded

  @property
  def lastContent(self):
    return self._lastContent

  @property
  def lastMessage(self):
    return self._lastMessage

  @property
  def lastResult(self):
    return self._lastResult

  def post(self, endpoint, data = None):
    return self._invoke('POST', endpoint, data)

  def put(self, endpoint, data = None):
    return self._invoke('PUT', endpoint, data)

  def query(self, endpoint, data = None):
    return self._invoke('QUERY', endpoint, data)

  def _setLastMessage(self, response):
    if 'Simpler-Message' in response.headers:
      self._lastMessage = response.headers['Simpler-Message']
    else:
      self._lastMessage = None

  def _setLastResult(self, response):
    self._lastContent = response.content
    try:
      self._lastResult = response.json()
    except:
      self._lastResult = response.text   