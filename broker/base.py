import pika
from config import RABBIT_MQ_SETTINGS


class Base:
    """Базовый класс клиента брокера"""
    def __init__(self):
        credentials = pika.PlainCredentials(
            RABBIT_MQ_SETTINGS['USER'],
            RABBIT_MQ_SETTINGS['PASSWORD'],
        )

        parameters = pika.ConnectionParameters(
            RABBIT_MQ_SETTINGS['HOST'],
            RABBIT_MQ_SETTINGS['PORT'],
            '/',
            credentials
        )

        self.channel = pika.BlockingConnection(parameters).channel()
        self.basic_properties = pika.BasicProperties(delivery_mode=2)
