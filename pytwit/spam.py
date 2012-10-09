# encoding=utf-8

from urllib import urlencode
from oauth2 import Client
import json

class SpamAPI:
  
  ''' field '''
  client = None
  api = 'http://api.twitter.com/1/'
  
  ''' constractor '''
  def __init__(self, client):
    self.client = client
  
  ''' each API method '''
  def report_spam(self, screen_name=None, user_id=None):
    if not screen_name and not user_id: raise Exception
    option = {}
    if screen_name: option['screen_name'] = screen_name
    if user_id: option['user_id'] = user_id
    url = self.api+'report_spam.json'
    res = self.client.request(url,'POST',urlencode(option))
    return json.loads(res)
  
