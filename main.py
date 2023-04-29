import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
sefariaDB = mongoClient["sefaria"]
sefariaDBTexts = sefariaDB["texts"]

masekhotQuery = {"versionTitle": 'William Davidson Edition - English', "$nor": tuple([{ "title": {"$regex": "^Mishnah"}}, {"title": {"$regex": "^Jerusalem Talmud Shekalim"}}, {"title": {"$regex": "^Introductions to the Babylonian Talmud"}}])}
masekhot = sefariaDBTexts.find(masekhotQuery)

for pasuk in masekhot:
  print(pasuk["title"])