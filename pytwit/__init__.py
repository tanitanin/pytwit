# encoding=utf-8

# TwitterAPI

from urllib import urlencode
from oauth2 import Client, Token, Consumer

# import APIs
from timeline import TimelineAPI
from status import StatusAPI
from user import UserAPI
from direct_message import DirectMessageAPI
from friendship import FriendshipAPI
from socialgraph import SocialgraphAPI
from account import AccountAPI
from favorite import FavoriteAPI
from notification import NotificationAPI
from block import BlockAPI
from spam import SpamAPI
from list import ListAPI
from search import SearchAPI
from geo import GeoAPI
from saved_search import SavedSearchAPI
from streaming import StreamingAPI


class TwitterAPI:
  
  ''' constructor '''
  def __init__(self, client):
    self.initAPI(client)
    return 
  
  ''' API initialize '''
  def initAPI(self, client):
    self.timeline = TimelineAPI(client)
    self.status = StatusAPI(client)
    self.user = UserAPI(client)
    self.dm = DirectMessageAPI(client)
    self.friendship = FriendshipAPI(client)
    self.social = SocialgraphAPI(client)
    self.account = AccountAPI(client)
    self.favorite = FavoriteAPI(client)
    self.notification = NotificationAPI(client)
    self.block = BlockAPI(client)
    self.list = ListAPI(client)
    self.search = SearchAPI(client)
    self.geo = GeoAPI(client)
    self.saved_search = SavedSearchAPI(client)
    self.streaming = StreamingAPI(client)
    return
  
  ''' load configuration file '''
  def load(self, path):
    dom = ET.parse(path).getroot()
    
    consumer_key = dom.findtext('.//consumer_key')
    consumer_secret = dom.findtext('.//consumer_secret')
    consumer = Consumer(consumer_key, consumer_secret)
    
    access_token = dom.findtext('.//access_token')
    access_token_secret = dom.findtext('.//access_token_secret')
    token = Token(access_token, access_token_secret)
    
    client = Client(consumer, token)
    self.initAPI(client)
    return
  
  ''' update '''
  def update(self, str):
    return self.status.update({'status':str})
  
