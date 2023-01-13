import asyncio
import pika

async def callback(channel, method, properties, body):
    print("Received message:", body.decode())
    await asyncio.sleep(1)
    print("Processed message.")
    channel.basic_ack(delivery_tag=method.delivery_tag)

async def consume():
    connection = pika.AsyncoreConnection(
        pika.ConnectionParameters("localhost")
    )
    channel = await connection.channel()

    await channel.queue_declare("hello")
    await channel.basic_consume("hello", callback)

    await connection.consume_messages()

loop = asyncio.get_event_loop()
loop.run_until_complete(consume())
