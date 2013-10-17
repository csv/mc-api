import json
import dataset 


db = dataset.connect('postgresql://brian:mc@localhost:5432/mc')
data = db['mc']
data.delete()

old_data = json.load(open('data.json'))

urls = []
new_data = []
for i, d in enumerate(old_data):
  if d['url'] not in urls:
    urls.append(d['url'])
    if d.has_key('img_links'):
      old_data[i]['img_links'] = "|".join(d['img_links'])
    else:
      old_data[i]['img_links'] = None
      old_data[i]['n_imgs'] = None
    new_data.append(old_data[i])

data.insert_many(new_data)