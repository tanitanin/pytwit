# encofing=utf-8

from urllib import urlencode
from oauth2 import Client
from urlparse import urlunparse
import json

import hosts

class StreamingAPI:
  
  ''' field '''
  client = None
  api_url = hosts.STREAM_HOST + "1.1"

  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def sample(self,delimited=None,stall_warnings=None):
    option = {}
    if delimited: option['delimited'] = delimited
    if stall_warnings: option['stall_warnings'] = stall_warnings
    url = self.api_url + '/statuses/sample.json?' + urlencode(option)
    st,res= self.client.request(url, 'GET')
    return st,json.loads(res)
  
  def filter(self,follow=None,track=None,locations=None,
             delimited=None,stall_warnings=None):
    option = {}
    if follow: option['follow'] = follow
    if track: option['track'] = track
    if locations: option['locations'] = locations
    if delimited: option['delimited'] = delimited
    if stall_warnings: option['stall_warnings'] = stall_warnings
    url = self.api_url + '/statuses/filter.json'
    st,res = self.client.request(url, 'POST', urlencode(option))
    return st,json.loads(res)
  
  def firehose(self,count=None,delimited=None,stall_warnings=None):
    option = {}
    if count: option['count'] = count
    if delimited: option['delimited'] = delimited
    if stall_warnings: option['stall_warnings'] = stall_warnings
    url = self.api_url + '/statuses/firehose.json?' + urlencode(option)
    st,res= self.client.request(url, 'GET')
    return st,json.loads(res)
  
  def user(self,replies=None,w=None,track=None,locations=None,
             delimited=None,stall_warnings=None):
    option = {}
    if w: option['with'] = w
    if replies: option['replies'] = replies
    if track: option['track'] = track
    if locations: option['locations'] = locations
    if delimited: option['delimited'] = delimited
    if stall_warnings: option['stall_warnings'] = stall_warnings
    url = hosts.USERSTREAM_HOST + '1.1' + '/user.json?' + urlencode(option)
    st,res = self.client.request(url, 'GET')
  

