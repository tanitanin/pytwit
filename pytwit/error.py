# encoding=utf-8


class TwitterError(Exception):
  def __init__(self,reason,response=None):
    self.reason = unicode(reason)
    self.response = response
  def __str__(self):
    return self.reason

class DuplicateError(TwitterError):
  pass

class ConnectionError(TwitterError):
  pass


