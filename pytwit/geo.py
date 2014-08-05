# encoding=utf-8

from urllib import urlencode
from oauth2 import Client
from urlparse import urlunparse
import json

class GeoAPI:
  
  ''' field '''
  client = None
  import hosts
  api = hosts.API_HOST + "/geo/"

  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def id(self,place_id):
    url = self.api+'id/'+place_id+'.json'
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def nearby_place(self, option):
    url = self.api+'nearby_place.json?'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def reverse_geocode(self,lat,long,accuracy=None,granularity=None,max_results=None,callback=None):
    option = {'lat':lat,'long':long}
    if accuracy: option['accuracy'] = accuracy
    if granularity: option['granularity'] = granularity
    if max_results: option['max_results'] = max_results
    if callback: option['callback'] = callback
    url = self.api+'reverse_geocode.json?'+urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def search(self,lat=None,long=None,query=None,ip=None,granularity=None,accuracy=None,max_results=None,contained_within=None,street_address=None,callback=None):
    option = {}
    if lat: option['lat'] = lat
    if long: option['long'] = long
    if query: option['query'] = query
    if ip: option['ip'] = ip
    if granularity: option['granularity'] = granularity
    if accuracy: option['accuracy'] = accuracy
    if max_results: option['max_results'] = max_results
    if contained_within: option['contained_within'] = contained_within
    if street_address: option['attribute:street_address'] = street_address
    if callback: option['callback'] = callback
    url = self.api + 'search.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def similar_place(self,lat,long,name,contained_within=None,street_address=None,callback=None):
    option = {'lat':lat,'long':long,'name':name}
    if contained_within: option['contained_within'] = contained_within
    if street_address: option['attribute:street_address'] = street_address
    if callback: option['callback'] = None
    url = self.api + 'similar_place.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)
  
  def place(self,name,contained_within,token,lat,long,street_address=None,callback=None):
    option = {'name':name,'lat':lat,'long':long,'token':token}
    option['contained_within'] = contained_within
    if street_address: option['attribute:street_address'] = street_address
    if callback: option['callback'] = callback
    url = self.api + 'place.json?' + urlencode(option)
    st,res = self.client.request(url,'GET')
    return st,json.loads(res)

