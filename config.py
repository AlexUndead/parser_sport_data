DB_SETTINGS = {
    'HOST': 'localhost',
    'USER': 'root',
    'NAME': 'kuznecov',
    'PASSWORD': '305712',
    'PORT': '3306',
}

RABBIT_MQ_SETTINGS = {
    'USER': 'mqadmin',
    'PASSWORD': 'mqadmin',
    'HOST': 'localhost',
    'PORT': 5672,
    'EXCHANGE_NAME': 'matches',  # названия обменника
    'QUEUE_NAME': 'match_queue',  # название очереди
}

FILE_PATH = {
    'SPORT': './files/sport/',  # директория файлов спорта
    'MATCH': './files/match/',  # директория файлов коэффициентов матчей
}

LOG_SETTINGS = {
    'BASE_PATH': './logs/',  # базовая директория логов
    'PARSER_LOG_NAME': 'parser_log.txt',  # названия файла с ошибками модуля парсинга
    'DB_LOG_NAME': 'db_log.txt',  # названия файла с ошибками модуля работы с бд
    'BROKER_LOG_NAME': 'broker_log.txt',  # названия файла с ошибками модуля брокер
}