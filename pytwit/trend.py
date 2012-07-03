# encoding=utf-8

from urllib import urlencode
from oauth2 import Client
import json

class TrendAPI:
  
  ''' field '''
  sapi  = 'http://search.twitter.com/1/trends/'
  api = 'http://api.twitter.com/1/trends/'
  
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  
  ''' api.trends API '''
  def available(self,lat=None,long=None):
    option = {}
    if lat: option['lat'] = lat
    if long: option['long'] = long
    url = self.api + 'available.json?' + urlencode(option)
    res = self.client.request(res,'GET')
    return json.loads(res)
  
  def daily(self,date=None,exclude=None):
    option = {}
    if date: opiton['date'] = date
    if exclude: option['exclude'] = exclude
    url = seld.api + 'daily.json?' + urlencode(option)
    res = self.client.request(res, 'GET')
    return json.loads(res)
  
  def weekly(self,date=None,exclude=None):
    option = {}
    if date: opiton['date'] = date
    if exclude: option['exclude'] = exclude
    url = seld.api + 'weekly.json?' + urlencode(option)
    res = self.client.request(res, 'GET')
    return json.loads(res)
  
  def trends(self, woeid, exclude=None):
    url = self.api + woeid + '.json'
    if exclude: url += '?exclude='+exclude
    res = self.client.request(res,'GET')
    return json.loads(res)
  
