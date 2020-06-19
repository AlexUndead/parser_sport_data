import os
from config import LOG_SETTINGS


class Base:
    """Базовый класс логера"""

    def __init__(self):
        self.full_path = LOG_SETTINGS['BASE_PATH'] + self.log_name  # log_name определяется в дочернем классе
        os.makedirs(LOG_SETTINGS['BASE_PATH'], exist_ok=True)
        mode = 'a'

        if not os.path.exists(self.full_path):
            mode = 'w+'

        self.file = open(
            self.full_path,
            mode
        )

    def __del__(self):
        self.file.close()

    def write(self, message):
        """записать сообщение в фаил лога"""
        self.file.write(message + '\n')
        print(self.except_message+self.full_path)
