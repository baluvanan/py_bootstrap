import pymongo
client = pymongo.MongoClient(host="localhost", port=27017)
db = client.movies
collection = db.cast

collection.insert_one({'name':'Kamal Hassan', 'dob':'7 November 1954'})