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
    'EXCHANGE_NAME': 'matches',
    'QUEUE_NAME': 'match_queue',
}

FILE_PATH = {
    'SPORT': './files/sport/',
    'MATCH': './files/match/',
}