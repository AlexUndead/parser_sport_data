import json
from .base import Base
from config import RABBIT_MQ_SETTINGS, FILE_PATH
from db.receive import Receive
from parser.match import Match


class Worker(Base):
    """Класс получения одного id матча из очереди"""

    def __init__(self):
        super().__init__()
        self.set_channel_settings()
        self.db_receive = Receive()
        self.parser_match = Match()

    def set_channel_settings(self):
        """установка начальных значений очереди"""
        self.channel.queue_declare(
            queue=RABBIT_MQ_SETTINGS['QUEUE_NAME'],
            durable=True,
        )
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue=RABBIT_MQ_SETTINGS['QUEUE_NAME'],
            on_message_callback=self.callback,
        )

    def callback(self, ch, method, properties, match_id):
        """обработка id матча полученного из очереди"""
        for match_id in self.db_receive.get_all_ids_match(match_id):
            self.parser_match.get_match_bets(FILE_PATH['MATCH']+match_id)


        ch.basic_ack(delivery_tag=method.delivery_tag)

    def run(self):
        """
        запуск процесса получающего и обрабатывающего данных из очереди
        """
        self.channel.start_consuming()
