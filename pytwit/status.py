# encoding=utf-8

from urllib import urlencode
from oauth2 import Client
from urlparse import urlunparse
import json

from error import TwitterError

class StatusAPI:
  
  ''' field '''
  client = None
  import hosts
  api = hosts.API_HOST+"/statuses/"
  
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  # update
  def update(self,status,in_reply_to_status_id=None,lat=None,long=None,place_id=None,display_coordinates=None,trim_user=None,include_entities=None):
    option = {'status':status}
    if in_reply_to_status_id: option['in_reply_to_status_id'] = in_reply_to_status_id
    if lat: option['lat'] = lat
    if long: option['long'] = long
    if place_id: option['place_id'] = place_id
    if display_coordinates: option['display_coordinates'] = display_coordinates
    if trim_user: option['trim_user'] = trim_user
    if include_entities: option['include_entities'] = include_entities
    url = self.api+'update.json'
    try:
      st, res = self.client.request(url,'POST',urlencode(option))
    except:
      raise Exception
    return st, json.loads(res)
  
  # update with media
  def update_with_media(self,status,media,possibly_sensitive=None,in_reply_to_status_id=None,lat=None,long=None,place_id=None,display_coordinates=None):
    option = {'status':status,'media':media}
    if in_reply_to_status_id: option['in_reply_to_status_id'] = in_reply_to_status_id
    if possibly_sensitive: option['possibly_sensitive'] = possibly_sensitive
    if lat: option['lat'] = lat
    if long: option['long'] = long
    if place_id: option['place_id'] = place_id
    if display_coordinates: option['display_coordinates'] = display_coordinates
    url = self.api+'update_with_media.json'
    try:
      st, res = self.client.request(url,'POST',urlencode(option))
    except:
      raise Exception
    return st, json.loads(res)
  
  # show
  def show(self,id,trim_user=None,include_entities=None,include_my_retweet=None):
    option = {}
    if trim_user: option['trim_user'] = trim_user
    if include_entities: option['include_entities'] = include_entities
    if include_my_retweet: option['include_my_retweet'] = include_my_retweet
    url = self.api+'show/'+str(id)+".json?" + urlencode(option)
    res = "{}"
    try:
      st, res = self.client.request(url,'GET')
    except:
      raise Exception
    return st, json.loads(res)
  
  # destroy
  def destroy(self,id,trim_user=None,include_entities=None):
    option = {}
    if trim_user: option['trim_user'] = trim_user
    if include_entities: option['include_entities'] = include_entities
    url = self.api+'destroy/'+str(id)+".json"
    try:
      st, res = self.client.request(url,'POST',urlencode(option))
    except:
      raise Exception
    return st, json.loads(res)
  
  # retweet
  def retweet(self,id,trim_user=None,include_entities=None):
    option = {}
    if trim_user: option['trim_user'] = trim_user
    if include_entities: option['include_entities'] = include_entities
    url = self.api+'retweet/'+str(id)+".json"
    try:
      st, res = self.client.request(url,'POST',urlencode(option))
    except:
      raise Exception
    return st, json.loads(res)
  
  # retweets
  def retweets(self,id,count=None,trim_user=None,include_entities=None):
    option = {}
    if count: option['count'] = count
    if trim_user: option['trim_user'] = trim_user
    if include_entities: option['include_entities'] = include_entities
    url = self.api + 'retweet/' + str(id) + ".json?" + urlencode(option)
    try:
      st, res = self.client.request(url,'GET',urlencode(option))
    except:
      raise Exception
    return st, json.loads(res)
  
  def retweeted_by(self,id,count=None,page=None):
    option = {}
    if count: option['count'] = count
    if page: option['page'] = page
    url = self.api + str(id) + "/retweeted_by.json?" + urlencode(option)
    try:
      st, res = self.client.request(url,'GET',urlencode(option))
    except:
      raise Exception
    return st, json.loads(res)
  
  def retweeted_by_ids(self,id,count=None,page=None,stringify_ids=None):
    option = {}
    if count: option['count'] = count
    if page: option['page'] = page
    if stringify_ids: option['stringify_ids'] = stringify_ids
    url = self.api + str(id) + "/retweeted_by/ids.json?" + urlencode(option)
    try:
      st, res = self.client.request(url,'GET',urlencode(option))
    except:
      raise Exception
    return st, json.loads(res)
  
  def oembed(self,id,url,maxwidth=None,hide_media=None,hide_thread=None,omit_script=None,align=None,related=None,lang=None):
    option = {'id':id,'url':url}
    if maxwidth: option['maxwidth'] = maxwidth
    if hide_media: option['hide_media'] = hide_media
    if hide_thread: option['hide_thread'] = hide_thread
    if omit_script: option['omit_script'] = omit_script
    if align: option['align'] = align
    if related: option['related'] = related
    if lang: option['lang'] = lang
    turl = self.api + "oembed.json?" + urlencode(option)
    try:
      st, res = self.client.request(turl,'GET',urlencode(option))
    except:
      raise Exception
    return st, json.loads(res)
  

