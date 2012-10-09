# encoding=utf-8

from urllib import urlencode
from oauth2 import Client
import json

class SearchAPI:
  
  ''' field '''
  client = None
  api  = 'http://search.twitter.com/1/'
  
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def search(self, option):
    url = self.api + 'search.json?' + urlencode(option)
    res = self.client.request(res,'GET')
    return json.loads(res)
  
  def trends(self, option):
    url = self.api + 'trends.json?' + urlencode(option)
    res = self.client.request(res,'GET')
    return json.loads(res)
  
  def current_trends(self, option):
    url = self.api + 'trends/current.json?' + urlencode(option)
    res = self.client.request(res,'GET')
    return json.loads(res)
  
  def daily_trends(self, option):
    url = self.api + 'trends/daily.json?' + urlencode(option)
    res = self.client.request(res,'GET')
    return json.loads(res)
  
  def weekly_trends(self, option):
    url = self.api + 'trends/weekly.json?' + urlencode(option)
    res = self.client.request(res,'GET')
    return json.loads(res)
  
  
