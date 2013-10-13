import redis
import pandas as pd 
import requests
import xml.etree.ElementTree as ET
import re
from thready import threaded
from scrape_page import scrape_page

def crawl(item):
  city, feed = item
  r = requests.get(feed)
  if r.status_code == 200:
    for child in ET.fromstring(r.content):
      
      # extract urls
      url = child.attrib.values()[0]

      # check if url is legit
      if re.search('[0-9]\\.html', url):
        
        # now check if url is already in database
        if not red.sismember('urls', url):
          print "adding %s..." % url

          # add url to urls list
          red.sadd('urls', url) 

          # scrape post
          post_data = scrape_page(url, city)

          # add post data to redis
          red.sadd('posts', post_data)

if __name__ == '__main__':
  red = redis.StrictRedis(host='localhost', port=6379, db=0)
  df = pd.read_csv('all_rss_feeds.csv')
  cities = [c for c in df.city]
  rss = [r for r in df.rss]
  items = zip(cities, rss)
  threaded(items, crawl, num_threads=100, max_queue=2000)
