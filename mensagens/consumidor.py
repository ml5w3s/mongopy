import pika

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaração da fila
channel.queue_declare(queue='Opa')

# Função de callback para processar a mensagem recebida
def callback(ch, method, properties, body):
    # Escreve a mensagem no arquivo
    with open('mensagens.txt', 'a') as f:
        f.write(body + '\n')

# Inscreve a função de callback na fila
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Esperando  mensagem. CTRL+C' para sair)
channel.start_consuming()
