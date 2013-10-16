import redis
import json

r = redis.StrictRedis(host='localhost', port=6379, db=0)

keys = r.keys()
data = []

for k in keys:
    if k != "urls":
      print "fetching %s" % k
      data += r.zrangebyscore(k, min=0, max=1e13)

print json.dumps([json.loads(d) for d in data])