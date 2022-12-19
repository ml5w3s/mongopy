import pymongo
import json

# Cria uma conexão com o MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Seleciona o banco de dados e a coleção
db = client["nome_do_banco"]
collection = db["nome_da_colecao"]

# Realiza a consulta e armazena os resultados em uma lista
results = []
cursor = collection.find({})
for document in cursor:
    results.append(document)

# Escreve os resultados em um arquivo JSON
with open("dados.json", "w") as outfile:
    json.dump(results, outfile)