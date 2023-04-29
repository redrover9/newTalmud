import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
sefariaDB = mongoClient["sefaria"]
sefariaDBTexts = sefariaDB["texts"]

masekhotQuery = {"versionTitle": 'William Davidson Edition - English', "$nor": tuple([{ "title": {"$regex": "^Mishnah"}}, {"title": {"$regex": "^Jerusalem Talmud Shekalim"}}, {"title": {"$regex": "^Introductions to the Babylonian Talmud"}}])}
masekhot = sefariaDBTexts.find(masekhotQuery)

f = open("gemara.txt", "a", encoding="utf-8")

for masekhet in masekhot:
    for sugya in masekhet["chapter"]:
        for psuk in sugya:
            f.write(psuk)
            f.write("\n")
f.close()