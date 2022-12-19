#coleção de exemplo
#{
#    "nome": "João",
#    "idade": 30,
#    "cidade": "São Paulo"
#}

# Seleciona a coleção
collection = db["nome_da_colecao"]

# Realiza a consulta
cursor = collection.find({"cidade": "São Paulo"})
for document in cursor:
    print(document)