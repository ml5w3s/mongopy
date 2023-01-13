import asyncio
import pika_async

async def send_message():
    connection = await pika_async.connect_robust("amqp://localhost/")
    channel = await connection.channel()
    await channel.queue_declare("hello")
    await asyncio.sleep(5)
    await channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    print("Sent 'Hello World!'")
    await connection.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(send_message())
