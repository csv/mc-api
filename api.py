import flask
import redis
import json

app = flask.Flask(__name__)

r = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route("/random")
def random():
  return r.srandmember('posts')

if __name__ == "__main__":
  app.debug = True
  app.run()