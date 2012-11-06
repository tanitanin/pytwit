# encoding=utf-8

from urllib import urlencode
from oauth2 import Client
import json

import hosts

class SearchAPI:
  
  ''' field '''
  client = None
  s_api  = 'http://search.twitter.com/1/'
  
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' Search API method '''
  def tweets(self,q,geoocde=None,lang=None,locale=None,result_type=None,
             count=None,until=None,since_id=None,max_id=None,
             include_entities=None,callback=None):
    option = {'q':q}
    if geoocde: option['geoocde'] = geoocde
    if lang: option['lang'] = lang
    if locale: option['locale'] = locale
    if result_type: option['result_type']
    if count: option['count'] = count
    if until: option['until'] = until
    if since_id: option['since_id'] = since_id
    if max_id: option['max_id'] = max_id
    if include_entities: option['include_entities'] = include_entities
    if callback: option['callback'] = callback
    url = hosts.API_HOST + '1.1' + '/search/' + 'tweets.json'
    url += '?' + urlencode(option)
    print url
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  ''' old API method '''
  #v1.1 not supported
  def search(self, option):
    url = self.s_api + 'search.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  #v1.1 not supported
  def trends(self, option):
    url = self.s_api + 'trends.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  #v1.1 not supported
  def current_trends(self, option):
    url = self.s_api + 'trends/current.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  #v1.1 not supported
  def daily_trends(self, option):
    url = self.s_api + 'trends/daily.json?' + urlencode(option)
    st,res = self.client.request(res,'GET')
    return st,json.loads(res)
  
  #v1.1 not supported
  def weekly_trends(self, option):
    url = self.s_api + 'trends/weekly.json?' + urlencode(option)
    st,res = self.client.request(res,'GET')
    return st,json.loads(res)
  
  
