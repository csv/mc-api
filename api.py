import flask
import redis
import json
from flask import request
import dateutil.parser
import re

app = flask.Flask(__name__)
red = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route("/random")
def random():
  return r.srandmember()

@app.route("/")
def dump_key():
  key = request.args.get('key', None)
  start = request.args.get('start', 0)
  end = request.args.get('end', 1e11)
  print key, start, end
  results = red.zrangebyscore(
    key, 
    min = start, 
    max = end
  )
  return json.dumps([json.loads(r) for r in results])

if __name__ == "__main__":
  app.debug = True
  app.run()