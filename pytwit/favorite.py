# encoding=utf-8

from urllib import urlencode
from oauth2 import Client
import json

class FavoriteAPI:
  
  ''' field '''
  client = None
  import hosts
  api = hosts.API_HOST
  
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def favorites(self,user_id=None,screen_name=None,count=None,since_id=None,max_id=None,page=None,include_entities=None):
    if not user_id and not screen_name: raise Exception
    option = {}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    url = self.api+'favorites.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def create(self,id,include_entities=None):
    url = self.api+'favorites/create/'+id+'.json'
    st,res = self.client.request(url,'POST',None)
    return st,json.loads(res)
  
  def destroy(self,id):
    url = self.api+'favorites/destroy/'+id+'.json'
    st,res = self.client.request(url,'POST',None)
    return st,json.loads(res)
  
