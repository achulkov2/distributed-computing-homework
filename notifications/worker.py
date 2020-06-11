import smtplib
import pika
import json

SERVER = 'smtp.gmail.com'
PORT = 587
EMAIL = 'dummymannequin@gmail.com'
PASS = ''


def callback(ch, method, properties, data):
    try:
        body = json.loads(data)
        server = smtplib.SMTP(SERVER, PORT)
        server.starttls()
        server.login(EMAIL, PASS)
        server.sendmail(EMAIL, body['recipient'], body['text'])
        server.close()
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except smtplib.SMTPException:
        return


connection = pika.BlockingConnection(pika.ConnectionParameters('mq', 5672, '/', pika.PlainCredentials('user', 'user')))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello', on_message_callback=callback)
channel.start_consuming()
