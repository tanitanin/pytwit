# encoding=utf-8

from urllib import urlencode
from oauth2 import Client
import json

class BlockAPI:
  
  ''' field '''
  client = None
  api = 'http://api.twitter.com/1/blocks/'
  
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def create(self,screen_name=None,user_id=None,include_entities=None,skip_status=None):
    option = {}
    if not screen_name and not user_id: raise Exception
    if screen_name: option['screen_name'] = screen_name
    if user_id: option['user_id'] = user_id
    if include_entities: option['include_entities'] = include_entities
    if skip_status: option['skip_status'] = skip_status
    url = self.api+'create.json'
    st,res= self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def destroy(self,screen_name=None,user_id=None,include_entities=None,skip_status=None):
    option = {}
    if not screen_name and not user_id: raise Exception
    if screen_name: option['screen_name'] = screen_name
    if user_id: option['user_id'] = user_id
    if include_entities: option['include_entities'] = include_entities
    if skip_status: option['skip_status'] = skip_status
    url = self.api+'destroy.json'
    st,res = self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def exists(self,screen_name=None,user_id=None,include_entities=None,skip_status=None):
    option = {}
    if not screen_name and not user_id: raise Exception
    if screen_name: option['screen_name'] = screen_name
    if user_id: option['user_id'] = user_id
    if include_entities: option['include_entities'] = include_entities
    if skip_status: option['skip_status'] = skip_status
    url = self.api+'exists.json?' + urlencode(option)
    st,res= self.client.request(url,'GET')
    return st,json.loads(res)
  
  def blocking(self,page=None,par_page=None,include_entities=None,skip_status=None,cursor=None):
    option = {}
    if page: option['page'] = page
    if par_page: option['par_page'] = par_page
    if include_entities: option['include_entities'] = include_entities
    if skip_status: option['skip_status'] = skip_status
    if cursor: option['cursor'] = cursor
    url = self.api+'blocking.json?'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def blocking_ids(self,stringify_ids=None,cursor=None):
    option = {}
    if stringify_ids: option['stringify_ids'] = stringify_ids
    if cursor: option['cursor'] = cursor
    url = self.api+'blocking/ids.json?'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
