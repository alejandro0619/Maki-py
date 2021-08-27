from tinydb import TinyDB, Query

db = TinyDB('db.json')

db.insert({
  'type': 'apple',
  'count': 5
})

get_all = db.all()
print(get_all)