import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()
ch.exchange_declare(exchange='logs', exchange_type='fanout')
result = ch.queue_declare(queue='', exclusive=True)

ch.queue_bind(exchange='logs', queue=result.method.queue)
print('Waiting for message ! ')


def callback(ch, method, properties, body):
    print(f'Received {body}')


ch.basic_consume(queue=result.method.queue, on_message_callback=callback, auto_ack=True)

ch.start_consuming()
