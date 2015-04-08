#!/usr/bin/python
# -*- coding: utf-8 -*-

from funciones import *
import json
from urllib import unquote


twitter_api = oauth_login()


search_results = twitter_api.search.tweets(q='Real Madrid', geocode='40.4173175,-3.702233699999965,700km')
save_json("trends.txt",search_results)