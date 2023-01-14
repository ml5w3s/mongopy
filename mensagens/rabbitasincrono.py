import pika
import asyncio

async def callback(ch, method, properties, body):
    # processar a mensagem
    print(body)

async def consume():
    connection = pika.AsyncoreConnection(pika.ConnectionParameters(host='localhost'))
    channel = await connection.channel()
    await channel.queue_declare(queue='myqueue')
    await channel.basic_consume(queue='myqueue', on_message_callback=callback)
    while True:
        await asyncio.sleep(5)

asyncio.run(consume())
