#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'miguel'
import twitter
import io
import json

#Función para la conexión.
def oauth_login():
    CONSUMER_KEY = 'KqqHIhsFjNrKHjmGfSnm9qLIl'
    CONSUMER_SECRET = 'Mi01ItdZX5VsKplh3Skg2Jalh3xSfnd1bF71sq18ezKK0kRNYJ'
    OAUTH_TOKEN = '3006010565-7MNx6Yjlw8bx03PQE6gjSj9sIFfnIqIUi04l8Jw'
    OAUTH_TOKEN_SECRET = '6Ke2ywfKx4pvLtOAX43FeUUHAZwn66jKPPFpoLIE6L7xd'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#Función para grabar la información en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Función para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()




