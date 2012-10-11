#!/usr/bin/python

from urllib import urlencode
from oauth2 import Client
from urlparse import urlunparse
import json

class TimelineAPI:
  
  ''' field '''
  client = None
  
  import hosts
  api_url = hosts.API_HOST+"1.1"+"/statuses/"
  
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def home_timeline(self,count=None,since_id=None,max_id=None,page=None,
                    trim_user=None,include_rts=None,include_entities=None,
                    exclude_replies=None,contributor_details=None):
    option = {}
    if count: option['count'] = count
    if since_id: option['since_id'] = since_id
    if max_id: option['max_id'] = max_id
    if page: option['page'] = page
    if trim_user: option['trim_user'] = trim_user
    if include_rts: option['include_rts'] = include_rts
    if include_entities: option['include_entities'] = include_entities
    if exclude_replies: option['exclude_replies'] = exclude_replies
    if contributor_details: option['contributor_details'] = contributor_details
    url = self.api_url + 'home_timeline.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def user_timeline(self,user_id=None,screen_name=None,count=None,
                    since_id=None,max_id=None,page=None,trim_user=None,
                    include_rts=None,include_entities=None,
                    exclude_replies=None,contributor_details=None):
    if not user_id and not screen_name: raise Exception
    option = {}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    if count: option['count'] = count
    if since_id: option['since_id'] = since_id
    if max_id: option['max_id'] = max_id
    if page: option['page'] = page
    if trim_user: option['trim_user'] = trim_user
    if include_rts: option['include_rts'] = include_rts
    if include_entities: option['include_entities'] = include_entities
    if exclude_replies: option['exclude_replies'] = exclude_replies
    if contributor_details: option['contributor_details'] = contributor_details
    url = self.api_url + 'user_timeline.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def mentions(self,count=None,since_id=None,max_id=None,page=None,
               trim_user=None,include_rts=None,include_entities=None,
               exclude_replies=None,contributor_details=None):
    option = {}
    if count: option['count'] = count
    if since_id: option['since_id'] = since_id
    if max_id: option['max_id'] = max_id
    if page: option['page'] = page
    if trim_user: option['trim_user'] = trim_user
    if include_rts: option['include_rts'] = include_rts
    if include_entities: option['include_entities'] = include_entities
    if exclude_replies: option['exclude_replies'] = exclude_replies
    if contributor_details: option['contributor_details'] = contributor_details
    url = self.api_url + 'mentions.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def retweeted_by_me(self,count=None,since_id=None,max_id=None,page=None,
                      trim_user=None,include_entities=None):
    option = {}
    if count: option['count'] = count
    if since_id: option['since_id'] = since_id
    if max_id: option['max_id'] = max_id
    if page: option['page'] = page
    if trim_user: option['trim_user'] = trim_user
    if include_entities: option['include_entities'] = include_entities
    url = self.api_url + 'retweeted_by_me.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def retweeted_to_me(self,count=None,since_id=None,max_id=None,page=None,
                      trim_user=None,include_entities=None):
    option = {}
    if count: option['count'] = count
    if since_id: option['since_id'] = since_id
    if max_id: option['max_id'] = max_id
    if page: option['page'] = page
    if trim_user: option['trim_user'] = trim_user
    if include_entities: option['include_entities'] = include_entities
    url = self.api_url + 'retweeted_to_me.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def retweets_of_me(self,count=None,since_id=None,max_id=None,page=None,
                     trim_user=None,include_entities=None):
    option = {}
    if count: option['count'] = count
    if since_id: option['since_id'] = since_id
    if max_id: option['max_id'] = max_id
    if page: option['page'] = page
    if trim_user: option['trim_user'] = trim_user
    if include_entities: option['include_entities'] = include_entities
    url = self.api_url + 'retweets_of_me.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def retweeted_by_user(self,user_id=None,screen_name=None,count=None,
                        since_id=None,max_id=None,page=None,trim_user=None,
                        include_entities=None):
    if not user_id and not screen_name: raise Exception
    option = {}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    if count: option['count'] = count
    if since_id: option['since_id'] = since_id
    if max_id: option['max_id'] = max_id
    if page: option['page'] = page
    if trim_user: option['trim_user'] = trim_user
    if include_entities: option['include_entities'] = include_entities
    url = self.api_url + 'retweeted_by_user.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def retweeted_to_user(self,user_id=None,screen_name=None,count=None,
                        since_id=None,max_id=None,page=None,trim_user=None,
                        include_entities=None):
    if not user_id and not screen_name: raise Exception
    option = {}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    if count: option['count'] = count
    if since_id: option['since_id'] = since_id
    if max_id: option['max_id'] = max_id
    if page: option['page'] = page
    if trim_user: option['trim_user'] = trim_user
    if include_entities: option['include_entities'] = include_entities
    url = self.api_url + 'retweeted_to_user.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  
#######
  def public_timeline(self,option):
    url = self.api_url+'public_timeline.json?'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def friends_timeline(self,option):
    url = self.api_url+'friends_timeline.json?'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)


