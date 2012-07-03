# encoding=utf-8

from urllib import urlencode
from oauth2 import Client
import json

class SavedSearchAPI:
  
  ''' field '''
  client = None
  api0 = 'http://api.twitter.com/1/'
  api  = 'http://api.twitter.com/1/saved_searches/'
  
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def saved_searches(self):
    url = self.api0 + 'saved_searches.json'
    res = self.client.request(res,'GET')
    return json.loads(res)
  
  def create(self, option):
    url = self.api + 'create.json'
    res = self.client.request(res,'POST',urlencode(option))
    return json.loads(res)
  
  def show(self, id):
    url = self.api + 'show/'+id+'.json'
    res = self.client.request(res,'GET')
    return json.loads(res)
  
  def destroy(self, id):
    url = self.api + 'destroy/'+id+'.json'
    res = self.client.request(res,'DELETE')
    return json.loads(res)
  