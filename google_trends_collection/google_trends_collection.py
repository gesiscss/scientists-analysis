'''
Created on 28 Jun 2016

@author: sennikta
'''
import pytrends
from pytrends.pyGTrends import pyGTrends
import os
import time
from random import randint
import urllib
# TODO solve encoding problem

base_dir = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(base_dir, 'data')
neighbors_dir = os.path.join(data_dir, 'neighbors')
google_trends_dir = os.path.join(data_dir, 'google_trends')
scientisis_dir = os.path.join(google_trends_dir, 'scientists\\')
topics_dir = os.path.join(google_trends_dir, 'topics\\')

def google_trend_crawler(name):
    google_username = "nobelprize.mt"
    google_password = "googletrendsparser"
    title = name.replace('_', ' ')
    title = title.rstrip().split('(')[0]
    title = title.decode("cp1252")
    #title = urllib.quote_plus(title.decode("utf-8"))
    title = title.encode('cp1252')
    connector  = pyGTrends(google_username, google_password)
    connector.request_report(title, hl='en-US')
    # wait a random amount of time between requests to avoid bot detection
    time.sleep(randint(5, 10))
    name = name.translate(None, ':*\'')
    name = name.decode("cp1252")
    name = urllib.quote_plus(name.encode("utf-8"))
    connector.save_csv("", name)
    return

counter = 0
filename =  os.path.join(neighbors_dir, 'topics_list_(spec_encoding)-1.txt')
with open(filename) as f:
    link_list = f.read().splitlines()   

for link in link_list:
    counter +=1
    print link
    
    print link.decode("cp1252").encode("utf-8")
    print counter
    google_trend_crawler(link)