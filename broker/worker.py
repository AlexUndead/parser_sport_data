import json
from .base import Base
from config import RABBIT_MQ_SETTINGS
from db.receive import Receive
from db.bet_saver import BetSaver
from parser.match import Match
from logger.broker import Broker
from pika.exceptions import AMQPError


class Worker(Base):
    """Класс обработки ставки матча полученного из очереди"""
    def __init__(self):
        super().__init__()
        self.set_channel_settings()
        self.db_receive = Receive()
        self.db_bet_saver = BetSaver()
        self.parser_match = Match()
        self.logger = Broker()

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
        for external_match_id in self.db_receive.get_all_ids_match(match_id):
            parse_match_data = self.parser_match.get_match_bets(external_match_id)
            if parse_match_data:
                self.db_bet_saver.save(parse_match_data)

        ch.basic_ack(delivery_tag=method.delivery_tag)

    def run(self):
        """
        запуск процесса получающего и обрабатывающего данных из очереди
        """
        try:
            self.channel.start_consuming()
        except AMQPError:
            self.logger.write(AMQPError.args[0])
