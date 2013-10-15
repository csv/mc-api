from bs4 import BeautifulSoup
import requests
import re
import dateutil.parser
import json

re_title = re.compile(r"(.*) - ([a-z]{1,2}4[a-z]{1,2})( - ([0-9]{1,2}))?( \((.*)\))?")
re_id = re.compile(r'(.*)/([0-9]+)\.html')

def parse_orientation_match(m):
  if m and m.group(2):
    orientation = m.group(2).strip()
    gender = orientation.split("4")[0]
    target = orientation.split("4")[1]
    return orientation, gender, target
  else:
    return None, None, None

def parse_city_to_slug(city):
  city = re.sub('/', ' ', city)
  city = re.sub('\\.', ' ', city).strip()
  return re.sub('\s+', '-', city).lower().strip()

def gen_redis_key(o):
  slug = parse_city_to_slug(o['city'])
  return '%s:%s' % (slug, o['orientation'])

def parse_title(soup):
  raw_title = soup.find("h2", {'class': 'postingtitle'}).text.strip()
  m = re_title.search(raw_title)  
  title = m.group(1).strip() if m else None
  orientation, gender, target = parse_orientation_match(m)
  age = int(m.group(4)) if m and m.group(4) else None
  location = m.group(6).strip() if m and m.group(6) else None
  return raw_title, title, orientation, age, location, gender, target

def parse_email(soup):
  raw_email = soup.find("section", {"class":"dateReplyBar"}).a.attrs['href'][7:]
  return raw_email.split('?')[0]

def parse_body(soup):
  return soup.find("section", {"id":"postingbody"}).text.strip()

def parse_date(soup):
  results = soup.findAll("p", {"class":"postinginfo"})
  date_string = [r.find('date').text for r in results if r.find('date')][0].strip()
  
  # reformat datestring, strip time zone
  date_string = re.sub(',', '', date_string)
  date_string = re.sub('\s+', ' ', date_string)
  date_string = ' '.join(date_string.split()[0:2])
  
  # return 
  return dateutil.parser.parse(date_string)

def parse_images(soup):
  img_div = soup.find("div", {"id":"thumbs"})
  if img_div:
    img_links = [a.attrs['href'] for a in img_div.findAll('a')]
    n_imgs = len(img_links)
  else:
    n_imgs = 0
    img_links = []
  return n_imgs, img_links

def scrape_page(url, city):
  r = requests.get(url)
  if r.status_code == 200:
    soup = BeautifulSoup(r.content)

    # parse date and title first
    dt = parse_date(soup)
    ts = int(dt.strftime("%s"))
    raw_title, title, orientation, age, location, gender, target = \
     parse_title(soup)
    
    n_imgs, img_links = parse_images(soup)
    
    output = dict(
      url = url,
      city = city,
      city_slug = parse_city_to_slug(city),
      raw_title = raw_title,
      title = title,
      orientation = orientation,
      gender = gender,
      target = target,
      age = age,
      location = location,
      email = parse_email(soup),
      body = parse_body(soup),
      timestamp = ts,
      datetime = dt.strftime("%Y-%m-%d %H:%M:%S"),
      year = dt.year,
      month = dt.month,
      day = dt.day,
      hour = dt.hour,
      min = dt.minute,
      weekday = dt.weekday(),
      n_imgs = n_imgs,
      img_links = img_links
    )

    key = gen_redis_key(output)
    # print "adding %s to key:%s with ts:%s" % (url, key, ts)
    
    return key, ts, json.dumps(output)

  else:
    return None

if __name__ == '__main__':
  print scrape_page('http://tijuana.es.craigslist.com.mx/mis/4130179087.html', 'tijuana')
