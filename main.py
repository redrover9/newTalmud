import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
sefariaDB = mongoClient["sefaria"]
sefariaDBTexts = sefariaDB["texts"]

myquery = { {"versionTitle": "William Davidson Edition - English", "$nor": [{"title": "/Mishnah/i"}, {"title": "/Jerusalem Talmud Shekalim/i"}, {"title": "/Introductions to the Babylonian Talmud/i"}]} }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)