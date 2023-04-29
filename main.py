import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
sefariaDB = mongoClient["sefaria"]
sefariaDBTexts = sefariaDB["texts"]

masekhtotQuery = {"versionTitle": "William Davidson Edition - English", "$nor": tuple([{"title": "/Mishnah/i"}, {"title": "/Jerusalem Talmud Shekalim/i"}, {"title": "/Introductions to the Babylonian Talmud/i"}])}
masekhtot = sefariaDBTexts.find(masekhtotQuery)

for pasuk in masekhtot:
  print(pasuk)