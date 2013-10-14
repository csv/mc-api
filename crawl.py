import redis
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
          red.sadd('urls', url)

          # scrape post
          key, rank, value = scrape_page(url, city)

          # add post data to redis
          red.zadd(key, rank, value)

if __name__ == '__main__':
  red = redis.StrictRedis(host='localhost', port=6379, db=0)
  cities = []
  feeds = []
  for line in open('all_rss_feeds.csv').read().split('\r')[1:]:
    row = line.split(",")
    feeds.append(row[0].strip())
    cities.append(row[2].strip())
  items = zip(cities, feeds)
  for i in items:
    print i[0], " - ", i[1]
  # go forth young scraper
  # threaded(items, crawl, num_threads=100, max_queue=2000)
  # # # debug mode #
  # [crawl(i) for i in items]

