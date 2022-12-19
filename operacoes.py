import pymongo

# Cria uma conexão com o MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Seleciona o banco de dados e a coleção
db = client["nome_do_banco"]
collection = db["nome_da_colecao"]

# Insere um documento
result = collection.insert_one({"nome": "João", "idade": 30})
print(result.inserted_id)

# Consulta todos os documentos
cursor = collection.find({})
for document in cursor:
    print(document)

# Atualiza um documento
result = collection.update_one({"nome": "João"}, {"$set": {"idade": 31}})
print(result.modified_count)

# Exclui um documento
result = collection.delete_one({"nome": "João"})
print(result.deleted_count)
