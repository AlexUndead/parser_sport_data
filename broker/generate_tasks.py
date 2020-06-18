from .base import Base
from config import RABBIT_MQ_SETTINGS


class GenerateTasks(Base):
    """Класс добавления id матчей в очередь"""
    def __init__(self, match_ids):
        super().__init__()
        self.match_ids = match_ids
        self.set_channel_settings()

    def set_channel_settings(self):
        """установка начальных настроек"""
        self.channel.exchange_declare(
            exchange=RABBIT_MQ_SETTINGS['EXCHANGE_NAME'],
            exchange_type='direct',
        )
        self.channel.queue_declare(
            queue=RABBIT_MQ_SETTINGS['QUEUE_NAME'],
            durable=True,
        )
        self.channel.queue_bind(
            exchange=RABBIT_MQ_SETTINGS['EXCHANGE_NAME'],
            queue=RABBIT_MQ_SETTINGS['QUEUE_NAME'],
        )

    def run(self):
        """запуск процесса добавления id матчей в очередь"""
        for match_id in self.match_ids:
            self.channel.basic_publish(
                exchange=RABBIT_MQ_SETTINGS['EXCHANGE_NAME'],
                routing_key=RABBIT_MQ_SETTINGS['QUEUE_NAME'],
                body=str(match_id),
                properties=self.basic_properties
            )

