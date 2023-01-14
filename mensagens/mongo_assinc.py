import asyncio
from pymongo import MongoClient

async def consume():
    client = MongoClient()
    db = client.mydatabase
    collection = db.mycollection
    while True:
        # Buscar dados do MongoDB
        cursor = collection.find()
        for document in cursor:
            # processar o documento
            print(document)
        await asyncio.sleep(5)

asyncio.run(consume())
