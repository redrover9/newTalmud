import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
sefariaDB = mongoClient["sefaria"]
sefariaDBTexts = sefariaDB["texts"]

masekhotQuery = {"versionTitle": 'William Davidson Edition - English', "$nor": tuple([{ "title": {"$regex": "^Mishnah"}}, {"title": {"$regex": "^Jerusalem Talmud Shekalim"}}, {"title": {"$regex": "^Introductions to the Babylonian Talmud"}}])}
masekhot = sefariaDBTexts.find(masekhotQuery)

f = open("gemara.txt", "a")

for masekhet in masekhot:
    for chapter in masekhet["chapter"]:
        f.write(chapter)
f.close()