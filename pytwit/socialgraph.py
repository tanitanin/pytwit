# encoding=utf-8

from oauth2 import Client
from urllib import urlencode
import json

class SocialgraphAPI:
  
  ''' field '''
  client = None
  api_frinds = 'http://api.twitter.com/1/friends/'
  api_followers = "http://api.twitter.com/1/followers/"
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def friends_ids(self,user_id=None,screen_name=None,cursor=None,stringify_ids=None):
    if not user_id and not screen_name: raise Exception
    option = {}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name']
    if cursor: option['cursor'] = cursor
    if stringify_ids: option['stringify_ids']
    url = api_frinds + 'ids.json?' + urlencode(option)
    code,res = self.client.request(url,'GET',urlencode(option))
    return code,json.loads(res)
  
  def followers_ids(self,user_id=None,screen_name=None,cursor=None,stringify_ids=None):
    if not user_id and not screen_name: raise Exception
    option = {}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name']
    if cursor: option['cursor'] = cursor
    if stringify_ids: option['stringify_ids']
    url = api_followers + 'ids.json?' + urlencode(option)
    code,res = self.client.request(url,'GET',urlencode(option))
    return code,json.loads(res)
  
