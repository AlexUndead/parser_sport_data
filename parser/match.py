import json


class Match:
    """Класс парсинга файлов видов матч"""
    def get_match_bets(self, file_path):
        """получение обработанной информации"""
        with open(file_path) as json_data:
            match_data = json.loads(json_data.readline())
