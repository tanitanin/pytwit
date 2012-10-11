# encoding=utf-8

from oauth2 import Client
from urllib import urlencode
import json

class UserAPI:
  
  ''' field '''
  client = None
  api0 = 'http://api.twitter.com/1/statuses/'
  api = "http://api.twitter.com/1/user/"
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def friends(self,option):
    url = api0+'friends.json'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def followers(self,option):
    url = api0+'followers.json'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def show(self,option):
    url = api+'show'
    if option['id'] == None:
      url += '.json?'+urlencode(option)
    else:
      url += '/'+option['id']+'.json'
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def lookup(self,option):
    url = api+'lookup.json'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def search(self,option):
    url = api+'search.json'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def suggestions(self,option):
    url = api+'suggestions.json'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def suggestions_category(self,option):
    url = api+'suggestions/category.json'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
