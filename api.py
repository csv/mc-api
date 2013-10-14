import flask
import redis
import json
from flask import request
import dateutil.parser
import re
from random import choice

app = flask.Flask(__name__)
red = redis.StrictRedis(host='localhost', port=6379, db=0)

# args for orientation=all
sexes = [
  "t", "tt", "m", "w", "mm", "ww", "wm", "mw"
]
orientations = ["%s4%s" %(s1, s2) for s1 in sexes for s2 in sexes] + ['None']

# slugify city arg:
def parse_city_to_slug(city):
  city = re.sub('/', ' ', city)
  city = re.sub('\\.', ' ', city).strip()
  return re.sub('\s+', '-', city).lower().strip()

@app.route('/random')
def random():
  key = red.randomkey()
  results = red.zrangebyscore(
          key, 
          min = 0, 
          max = 1e11
        )
  return choice(results)

@app.route("/")
def query():
  # parse args
  city = parse_city_to_slug(request.args.get('city', 'new york city'))
  orientation = request.args.get('orientation', 'all')
  start = request.args.get('start', 0)
  end = request.args.get('end', 1e11)
  
  if orientation=="all":
    results = []
    for o in orientations:
        key = "%s:%s" % (city, o)
        result = red.zrangebyscore(
          key, 
          min = start, 
          max = end
        )
        results += result

  else:
    key = "%s:%s" % (city, orientation)
    results = red.zrangebyscore(
      key, 
      min = start, 
      max = end
    )

  # turn it into a json list
  return "[%s]" % ",".join(results)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)