from pymongo import MongoClient
import pika

# Conexão com o MongoDB
client = MongoClient()
db = client.mydatabase
collection = db.mycollection

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='myqueue')

# Recuperar dados do MongoDB e armazená-los na fila RabbitMQ
cursor = collection.find()
for document in cursor:
    channel.basic_publish(exchange='', routing_key='myqueue', body=document)

print("Dados armazenados na fila com sucesso.")
connection.close()
