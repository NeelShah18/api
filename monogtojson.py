from pyhomgo import MongoClient
from bson import Binary, Code
from bson.json_util import dumps
import json

client = MongoClient('address')
db = client['Database_name']
cursor = db.Name_of_collection.find({"borough": "Manhattan"}) #<- it is query
json_string = dumps(cursor)

with open('data.json', 'w') as outfile:
    json.dump(json_string, outfile)
