from config import LOG_SETTINGS
from logger.base import Base


class DB(Base):
    """Класс логера работы с бд"""
    def __init__(self):
        self.log_name = LOG_SETTINGS['DB_LOG_NAME']
        self.except_message = 'Ошибка в модуле работы с бд. ' \
                              'Подробнее можно посмотреть в файле '
        super().__init__()
