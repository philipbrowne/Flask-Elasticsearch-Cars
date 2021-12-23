import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='host.docker.internal'))
channel = connection.channel()

channel.queue_declare(queue='cars')

def send_message(body):
    channel.basic_publish(exchange='', routing_key='cars', body=body)
    print (f'Sent Msg')