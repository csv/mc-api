import flask
from flask import request
import json
import dataset
import dateutil.parser
import re
import StringIO
import csv

app = flask.Flask(__name__)
db = dataset.connect('sqlite:///test.db')


@app.route("/")
def query():
  # parse args  
  query = request.args.get('q', None) 
  return json.dumps([r for r in db.query(query)])
  
if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0', port=5000)