# encoding=utf-8

from urllib import urlencode
from oauth2 import Client
import json

class FriendshipAPI:
  
  ''' field '''
  client = None
  api0 = "http://api.twitter.com/1/"
  api = 'http://api.twitter.com/1/friendships/'
  
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def show(self,source_id=None,source_screen_name=None,target_id=None,target_screen_name=None):
    option = {}
    if source_id: option['source_id'] = source_id
    if source_screen_name: option['source_screen_name'] = source_screen_name
    if target_id: option['target_id'] = target_id
    if target_screen_name: option['target_screen_name'] = target_screen_name
    url = self.api+'show.json?'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def create(self,user_id=None,screen_name=None,follow=None):
    if not user_id and not screen_name: raise Exception
    option = {}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    if follow: option['follow'] = follow
    url = self.api+'create.json'
    st,res = self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def destroy(self,user_id=None,screen_name=None,include_entities=None):
    if not user_id and not screen_name: raise Exception
    option = {}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    if include_entities: option['include_entities'] = include_entities
    url = self.api+'destroy.json'
    st,res = self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def exists(self,user_id_a=None,screen_name_a=None,user_id_b=None,screen_name_b=None):
    if not user_id_a and not screen_name_a: raise Exception
    if not user_id_b and not screen_name_b: raise Exception
    option = {}
    if user_id_a: option['user_id_a'] = user_id_a
    if user_id_b: option['user_id_b'] = user_id_b
    if screen_name_a: option['screen_name_a'] = screen_name_a
    if screen_name_b: option['screen_name_b'] = screen_name_b
    url = self.api+'exists.json'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def update(self,user_id=None,screen_name=None,device=None,retweets=None):
    if not user_id and not screen_name: raise Exception
    option = {}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    if device: option['device'] = device
    if retweets: option['retweets'] = retweets
    url = self.api+'update.json'
    st,res = self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def lookup(self,user_id=None,screen_name=None):
    if not user_id and not screen_name: raise Exception
    option = {}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    url = self.api + 'lookup.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def incoming(self,cursor=None,stringigy_ids=None):
    option = {}
    if cursor: option['cursor'] = cursor
    if stringigy_ids: option['stringigy_ids'] = stringigy_ids
    url = self.api + 'incoming.json?'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def outgoing(self,cursor=None,stringigy_ids=None):
    option = {}
    if cursor: option['cursor'] = cursor
    if stringigy_ids: option['stringigy_ids'] = stringigy_ids
    url = self.api + 'outgoing.json?'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def ids(self,user_id=None,screen_name=None,cursor=None,stringigy_ids=None):
    if not user_id and not screen_name: raise Exception
    option = {}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    if cursor: option['cursor'] = cursor
    if stringigy_ids: option['stringigy_ids'] = stringigy_ids
    url = self.api + 'ids.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)


