from config import LOG_SETTINGS
from logger.base import Base


class Parser(Base):
    """Класс логера парсера"""
    def __init__(self):
        self.log_name = LOG_SETTINGS['PARSER_LOG_NAME']
        self.except_message = 'Ошибка в модуле парсинга файлов. ' \
                              'Подробнее можно посмотреть в файле '
        super().__init__()
