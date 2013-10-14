from bs4 import BeautifulSoup
import requests
import re
import dateutil.parser
import json
import string

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
  # remove slashes
  city = re.sub('/', ' ', city)
  # remove periods
  city = re.sub('\\.', ' ', city)
  # convert spaces to dashes
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
  return soup.find("section", {"class":"dateReplyBar"}).a.attrs['href'][7:]

def parse_body(soup):
  return soup.find("section", {"id":"postingbody"}).text.strip()

def parse_date(soup):
  results = soup.findAll("p", {"class":"postinginfo"})
  date_string = [r.find('date').text for r in results if r.find('date')][0]
  return dateutil.parser.parse(date_string)

def scrape_page(url, city):
  r = requests.get(url)
  if r.status_code == 200:
    soup = BeautifulSoup(r.content)

    # parse date and title first
    dt = parse_date(soup)
    raw_title, title, orientation, age, location, gender, target = parse_title(soup)
    ts = int(dt.strftime("%s"))
    output = dict(
      url = url,
      city = city,
      slug = parse_city_to_slug(city),
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
      weekday = dt.weekday()
    )

    key = gen_redis_key(output)
    # print "adding %s to key:%s with ts:%s" % (url, key, ts)
    
    return key, ts, json.dumps(output)

  else:
    return None

if __name__ == '__main__':
  print scrape_page('http://fortsmith.craigslist.org/mis/4035763349.html', 'fortsmith')