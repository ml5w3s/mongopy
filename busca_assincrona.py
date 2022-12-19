import asyncio
import motor.motor_asyncio

async def main():
    # Cria uma conexão com o MongoDB
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")

    # Seleciona o banco de dados e a coleção
    db = client["nome_do_banco"]
    collection = db["nome_da_colecao"]

    # Realiza a consulta
    cursor = await collection.find({"cidade": "São Paulo"}).to_list(length=100)
    for document in cursor:
        print(document)

asyncio.run(main())