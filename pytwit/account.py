# encoding=utf-8

from urllib import urlencode
from oauth2 import Client
import json

class AccountAPI:
  
  ''' field '''
  import hosts
  api = hosts.API_HOST + '/account/'
  
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def rate_limit_status(self,include_entities=None,skip_status=None):
    url = self.api+'rate_limit_status.json'
    st, res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def verify_credentials(self,include_entities=None,skip_status=None):
    option={}
    if include_entities:
      option['include_entities'] = include_entities
    if skip_status:
      option['skip_status'] = skip_status
    url = self.api+'verify_credentials.json'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def end_session(self):
    url = self.api+'end_session.json'
    st,res = self.client.request(url,'POST',urlencode({}))
    return st,json.loads(res)
  
  def update_profile(self,name=None,url=None,location=None,description=None,include_entities=None,skip_status=None):
    option={}
    if name: option['name'] = name
    if url: option['url'] = url
    if location: option['location'] = location
    if description: option['description']
    if include_entities:
      option['include_entities'] = include_entities
    if skip_status:
      option['skip_status'] = skip_status
    url = self.api+'update_profile.json'
    st,res = self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def update_profile_colors(self, profile_background_color=None,
                            profile_link_color=None,
                            profile_sidebar_border_color=None,
                            profile_sidebar_fill_color=None,
                            profile_text_color=None,include_entities=None,
                            skip_status=None):
    option = {}
    if profile_background_color:
      option['profile_background_color'] = profile_background_color
    if profile_link_color:
      option['profile_link_color'] = profile_link_color
    if profile_sidebar_border_color:
      option['profile_sidebar_border_color'] = profile_sidebar_border_color
    if profile_sidebar_fill_color:
      option['profile_sidebar_fill_color'] = profile_sidebar_fill_color
    if profile_text_color:
      option['profile_text_color'] = profile_text_color
    if include_entities:
      option['include_entities'] = include_entities
    if skip_status:
      option['skip_status'] = skip_status
    url = self.api+'update_profile_colors.json'
    st,res = self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def update_profile_image(self,image,include_entities=None,skip_status=None):
    option = {'image':image}
    if include_entities:
      option['include_entities'] = include_entities
    if skip_status:
      option['skip_status'] = skip_status
    url = self.api+'update_profile_image.json'
    st,res = self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def update_profile_background_image(self,image=None,tile=None,include_entities=None,skip_status=None):
    option = {}
    if image:
      option['image'] = image
    if tile:
      option['tile'] = tile
    if include_entities:
      option['include_entities'] = include_entities
    if skip_status:
      option['skip_status'] = skip_status
    url = self.api+'update_profile_background_image.json'
    st,res = self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)
  
  def totals(self):
    url = self.api+'totals.json'
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def get_settings(self):
    url = self.api+'settings.json'
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
    
  def post_settings(self,trend_location_woeid=None,sleep_time_enable=None,start_sleep_time=None,end_sleep_time=None,timezone=None,lang=None):
    option = {}
    if trend_location_woeid:
      option['trend_location_woeid'] = trend_location_woeid
    if sleep_time_enable:
      option['sleep_time_enable'] = sleep_time_enable
    if start_sleep_time:
      option['start_sleep_time'] = start_sleep_time
    if end_sleep_time:
      option['end_sleep_time'] = end_sleep_time
    if timezone:
      option['timezone'] = timezone
    if lang:
      option['lang'] = lang
    url = self.api+'settings.json'
    st,res = self.client.request(url,'POST',urlencode(option))
    return st,json.loads(res)

