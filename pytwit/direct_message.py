# encoding=utf-8

from urllib import urlencode
from oauth2 import Client
import json

import hosts

class DirectMessageAPI:
  
  ''' field '''
  client = None
  api_base_url = hosts.API_HOST + '1.1' + '/'
  api_url = hosts.API_HOST + '1.1' + '/direct_messages/'
  
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def direct_messages(self,since_id=None,max_id=None,count=None,page=None,include_enitities=None,skip_status=None):
    option = {}
    if since_id: option['since_id'] = since_id
    if max_id: option['max_id'] = max_id
    if count: option['count'] = count
    if page: option['page'] = page
    if include_enitities: option['include_enitities'] = include_enitities
    if skip_status: option['skip_status'] = skip_status
    url = self.api_base_url+'direct_message.json?'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def sent(self,since_id=None,max_id=None,count=None,page=None,include_enitities=None,skip_status=None):
    option = {}
    if since_id: option['since_id'] = since_id
    if max_id: option['max_id'] = max_id
    if count: option['count'] = count
    if page: option['page'] = page
    if include_enitities: option['include_enitities'] = include_enitities
    if skip_status: option['skip_status'] = skip_status
    url = self.api_url+'sent.json?'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def new(self,text,user_id=None,screen_name=None):
    if not user_id and not screen_name: raise Exception
    option = {'text':text}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    url = self.api_url+'new.json'
    st,res = self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def show(self,id):
    url = self.api_url+'show.json?id='+str(id)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def destroy(self,id,include_enitities=None):
    url = self.api_url+'destroy.json?id=' + str(id)
    if include_enitities: url += '&include_enitities=' + include_enitities
    st,res = self.client.request(url,'DELETE',urlencode(option))
    return st,json.loads(res)
  
