#Realiza a busco com 2 critérios
cursor = collection.find({"$and": [{"cidade": "São Paulo"}, {"idade": {"$gt": 25}}]})
for document in cursor:
    print(document)
