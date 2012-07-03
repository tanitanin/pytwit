# encofing=utf-8

from urllib import urlencode
from oauth2 import Client
from urlparse import urlunparse
import json

class StreamingAPI:
  
  ''' field '''
  client = None
  api = "http://stream.twitter.com/1/statuses/"

  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def sample(self,option):
    url = self.api + 'sample.json?' + urlencode(option)
    res= self.client.request(url, 'GET')
    return json.loads(res)
  
  def filter(self,option):
    url = self.api + 'filter.json'
    res = self.client.request(url, 'POST', urlencode(option))
    return json.loads(res)
  