pytwit
======

Twitter API library with python

How to install
--------------

setup.pyを実行してください

How to use
----------

    from oauth2 import Client,Token,Consumer
    from pytwit import TwitterAPI
    
    consumer_key    = "hoge"
    consumer_secret = "huga"
    access_token    = "foo"
    access_token_secret = "bar"
    
    api = TwitterAPI(Client(Consumer(consumer_key,consumer_secret),
                            Token(access_token,access_token_secret))
    
    api.status.update("つぶやきたいことをここへ入れる")

Future
------

* 不具合の修正
* ユーザストリームへの対応

Contact
-------

Twitter account: @tanitanin

