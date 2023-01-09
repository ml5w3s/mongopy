import pika

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaração da fila
channel.queue_declare(queue='opa')

# Envia a mensagem
channel.basic_publish(exchange='', routing_key='hello', body='salve!')
print(" [x] Enviar um salve!'")

# Fecha a conexão
connection.close()
