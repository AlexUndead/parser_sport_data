from config import LOG_SETTINGS
from logger.base import Base


class Broker(Base):
    """Класс логера брокера"""
    def __init__(self):
        self.log_name = LOG_SETTINGS['BROKER_LOG_NAME']
        self.except_message = 'Ошибка в модуле работы клиента брокера. ' \
                              'Подробнее можно посмотреть в файле '
        super().__init__()
