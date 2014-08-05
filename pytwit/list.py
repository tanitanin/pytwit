# encoding=utf-8

from urllib import urlencode
from oauth2 import Client
import json

class ListAPI:
  
  ''' field '''
  client = None
  import hosts
  api = hosts.API_HOST
  lapi = hosts.API_HOST + "/lists/"
  
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def lists(self,user_id=None,screen_name=None,cursor=None):
    if not user_id and not screen_name: raise Exception
    option = {}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    if cursor: option['cursor'] = cursor
    url = self.api + 'lists.json?' + urlencode(option)
    st,res= self.client.request(url,'GET')
    return st,json.loads(res)
  
  def create(self,name,mode=None,description=None):
    option = {'name':name}
    if mode: option['mode'] = mode
    if description: option['description'] = description
    url = self.lapi + 'create.json'
    st,res= self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def update(self,list_id=None,slug=None,name=None,mode=None,description=None,owner_screen_name=None,owner_id=None):
    if not list_id and not slug: raise Exception
    option = {}
    if list_id: option['list_id'] = list_id
    if slug:
      if not owner_screen_name and not owner_id: raise Exception
      option['slug'] = slug
    if name: option['name'] = name
    if mode: option['mode'] = mode
    if description: option['description'] = description
    if owner_screen_name: option['owner_screen_name'] = owner_screen_name
    if owner_id: option['owner_id'] = owner_id
    url = self.lapi + 'update.json'
    st,res= self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def destroy(self,list_id=None,slug=None,owner_screen_name=None,owner_id=None):
    if not list_id and not slug: raise Exception
    option = {}
    if list_id: option['list_id'] = list_id
    if slug: 
      if not owner_screen_name and not owner_id: raise Exception
      option['slug'] = slug
    if owner_screen_name: option['owner_screen_name'] = owner_screen_name
    if owner_id: option['owner_id'] = owner_id
    url = self.lapi + 'destroy.json'
    st,res= self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def all(self,user_id=None,screen_name=None):
    option = {}
    if user_id: optio['user_id'] = user_id
    if screen_name: option['screen_name']= screen_name
    url = self.lapi + 'all.json?' + urlencode(option)
    st,res= self.client.request(url,'GET')
    return st,json.loads(res)
  
  def statuses(self,list_id=None,slug=None,owner_screen_name=None,owner_id=None,since_id=None,max_id=None,page=None,par_page=None,include_entities=None,include_rts=None):
    if not list_id and not slug: raise Exception
    option = {}
    if list_id: option['list_id'] = list_id
    if slug: 
      if not owner_screen_name and not owner_id: raise Exception
      option['slug'] = slug
    if owner_screen_name: option['owner_screen_name'] = owner_screen_name
    if owner_id: option['owner_id'] = owner_id
    if since_id: option['since_id'] = since_id
    if max_id: option['max_id'] = max_id
    if page: option['page'] = page
    if par_page: option['par_page'] = par_page
    if include_entities: option['include_entities'] = include_entities
    if include_rts: option['include_rts'] = include_rts
    url = self.lapi + 'statuses.json?' + urlencode(option)
    st,res= self.client.request(url,'GET')
    return st,json.loads(res)
  
  def statuses(self,list_id=None,slug=None,owner_screen_name=None,owner_id=None,since_id=None,max_id=None,page=None,par_page=None,include_entities=None,include_rts=None):
    if not list_id and not slug: raise Exception
    option = {}
    if list_id: option['list_id'] = list_id
    if slug: 
      if not owner_screen_name and not owner_id: raise Exception
      option['slug'] = slug
    if owner_screen_name: option['owner_screen_name'] = owner_screen_name
    if owner_id: option['owner_id'] = owner_id
    url = self.lapi + 'show.json?' + urlencode(option)
    st,res= self.client.request(url,'GET')
    return st,json.loads(res)
  
  def members(self,list_id=None,slug=None,owner_screen_name=None,owner_id=None,cursor=None,include_entities=None,skip_status=None):
    if not list_id and not slug: raise Exception
    option = {}
    if list_id: option['list_id'] = list_id
    if slug: 
      if not owner_screen_name and not owner_id: raise Exception
      option['slug'] = slug
    if owner_screen_name: option['owner_screen_name'] = owner_screen_name
    if owner_id: option['owner_id'] = owner_id
    if cursor: option['cursor'] = cursor
    if include_entities: option['include_entities'] = include_entities
    if skip_status: option['skip_status'] = skip_status
    url = self.lapi + 'members.json?' + urlencode(option)
    st,res= self.client.request(url,'GET')
    return st,json.loads(res)
  
  def memberships(self,user_id=None,screen_name=None,cursor=None,filter_to_owned_lists=None):
    option = {}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    if cursor: option['cursor'] = cursor
    if filter_to_owned_lists: option['filter_to_owned_lists'] = filter_to_owned_lists
    url = self.lapi + 'memberships.json?' + urlencode(option)
    st,res= self.client.request(url,'GET')
    return st,json.loads(res)
  
  def subscribers(self,list_id=None,slug=None,owner_screen_name=None,owner_id=None,cursor=None,include_entities=None,include_rts=None):
    if not list_id and not slug: raise Exception
    option = {}
    if list_id: option['list_id'] = list_id
    if slug: 
      if not owner_screen_name and not owner_id: raise Exception
      option['slug'] = slug
    if owner_screen_name: option['owner_screen_name'] = owner_screen_name
    if cursor: option['cursor'] = cursor
    if include_entities: option['include_entities'] = include_entities
    if include_rts: option['include_rts'] = include_rts
    url = self.lapi + 'subscribers.json?' + urlencode(option)
    st,res= self.client.request(url,'GET')
    return st,json.loads(res)
  
  def subscriptions(self,user_id=None,screen_name=None,count=None,cursor=None):
    if not user_id and not screen_name: raise Exception
    option = {}
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    if count: option['count'] = count
    if cursor: option['cursor'] = cursor
    url = self.lapi + 'subscriptions.json?' + urlencode(option)
    st,res= self.client.request(url,'GET')
    return st,json.loads(res)
  
  ''' members '''
  def show_members(self,list_id=None,slug=None,owner_screen_name=None,owner_id=None,user_id=None,screen_name=None,include_entities=None,skip_status=None):
    if not list_id and not slug: raise Exception
    if not user_id and not screen_name: raise Exception
    option = {}
    if list_id: option['list_id'] = list_id
    if slug: 
      if not owner_screen_name and not owner_id: raise Exception
      option['slug'] = slug
    if owner_screen_name: option['owner_screen_name'] = owner_screen_name
    if owner_id: option['owner_id'] = owner_id
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    if include_entities: option['include_entities'] = include_entities
    if skip_status: option['skip_status'] = skip_status
    url = self.lapi + 'members/show.json?' + urlencode(option)
    st,res= self.client.request(url,'GET')
    return st,json.loads(res)
  
  def create_members(self,list_id=None,slug=None,owner_screen_name=None,owner_id=None,user_id=None,screen_name=None):
    if not list_id and not slug: raise Exception
    if not user_id and not screen_name: raise Exception
    option = {}
    if list_id: option['list_id'] = list_id
    if slug: 
      if not owner_screen_name and not owner_id: raise Exception
      option['slug'] = slug
    if owner_screen_name: option['owner_screen_name'] = owner_screen_name
    if owner_id: option['owner_id'] = owner_id
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    url = self.lapi + 'members/create.json'
    st,res= self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def destroy_members(self,list_id=None,slug=None,owner_screen_name=None,owner_id=None,user_id=None,screen_name=None):
    if not list_id and not slug: raise Exception
    if not user_id and not screen_name: raise Exception
    option = {}
    if list_id: option['list_id'] = list_id
    if slug: 
      if not owner_screen_name and not owner_id: raise Exception
      option['slug'] = slug
    if owner_screen_name: option['owner_screen_name'] = owner_screen_name
    if owner_id: option['owner_id'] = owner_id
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    url = self.lapi + 'members/destroy.json'
    st,res= self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  ''' subscribers '''
  def show_subscribers(self,list_id=None,slug=None,owner_screen_name=None,owner_id=None,user_id=None,screen_name=None,include_entities=None,skip_status=None):
    if not list_id and not slug: raise Exception
    if not user_id and not screen_name: raise Exception
    option = {}
    if list_id: option['list_id'] = list_id
    if slug: 
      if not owner_screen_name and not owner_id: raise Exception
      option['slug'] = slug
    if owner_screen_name: option['owner_screen_name'] = owner_screen_name
    if owner_id: option['owner_id'] = owner_id
    if user_id: option['user_id'] = user_id
    if screen_name: option['screen_name'] = screen_name
    if include_entities: option['include_entities'] = include_entities
    if skip_status: option['skip_status'] = skip_status
    url = self.lapi + 'subscribers/show.json?' + urlencode(option)
    st,res= self.client.request(url,'GET')
    return st,json.loads(res)
  
  def create_subscribers(self,list_id=None,slug=None,owner_screen_name=None,owner_id=None):
    if not list_id and not slug: raise Exception
    if not user_id and not screen_name: raise Exception
    option = {}
    if list_id: option['list_id'] = list_id
    if slug: 
      if not owner_screen_name and not owner_id: raise Exception
      option['slug'] = slug
    if owner_screen_name: option['owner_screen_name'] = owner_screen_name
    if owner_id: option['owner_id'] = owner_id
    url = self.lapi + 'subscribers/create.json'
    st,res= self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def destroy_subscribers(self,list_id=None,slug=None,owner_screen_name=None,owner_id=None):
    if not list_id and not slug: raise Exception
    if not user_id and not screen_name: raise Exception
    option = {}
    if list_id: option['list_id'] = list_id
    if slug: 
      if not owner_screen_name and not owner_id: raise Exception
      option['slug'] = slug
    if owner_screen_name: option['owner_screen_name'] = owner_screen_name
    if owner_id: option['owner_id'] = owner_id
    url = self.lapi + 'subscribers/destroy.json'
    st,res= self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
