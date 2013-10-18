import dataset
import random
import requests
import xml.etree.ElementTree as ET
import re
from thready import threaded
from scrape_page import scrape_page, parse_city_to_slug
from datetime import datetime

# initialize postgres database
db = dataset.connect('postgresql://brian:mc@localhost:5432/mc')
data = db['mc']

# crawl a single feed
def crawl(item):
  city, feed = item
  r = requests.get(feed)
  if r.status_code == 200:
    for child in ET.fromstring(r.content):
      
      # extract urls
      url = child.attrib.values()[0]

      # check if url is legit
      if re.search('[0-9]\\.html', url):

        # scrape post
        print "scraping data from %s @ %s" % (url, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        page_data = scrape_page(url, city)
        
        # add post data to safely database
        data.upsert(page_data, "url")
          

if __name__ == '__main__':

  # generate input
  cities = []
  feeds = []
  for line in open('feeds/all_rss_feeds.csv').read().split('\r')[1:]:
    row = line.split(",")
    feeds.append(row[0].strip())
    cities.append(parse_city_to_slug(row[2].strip()))

  # randomly shuffle items to hit different rss feeds first
  items = zip(cities, feeds)

  # go forth young scraper
  threaded(items, crawl, num_threads=10, max_queue=200)

  # print md for readme
  # for i in items:
  #   print "[%s](%s)<br/>" % i

