import json
import os
from config import FILE_PATH


class Sport:
    """Класс парсинга файлов видов спорта"""
    sport_types = 'SS'
    sport_name = 'N'
    championship_types = 'CC'
    championship_name = 'N'
    matches = 'GG'
    match_home = 'H'
    match_away = 'A'
    match_id = 'I'
    match_date = 'S'
    event_type = 'T'
    parsed_data = []

    def is_match_data(self, match):
        """проверка непосредственного исхода матча"""
        return True if match[self.event_type] == '' and match['A'] != 'Гости (голы)' else False

    def get_duplicate_match(self, match):
        """получение дубликаты матчей"""
        return [duplicate[self.match_id] for duplicate in match[self.matches]]

    def processing_match_data(self, sport_name, championship_name, matches):
        """обрабока данных матча"""
        for match in matches:
            if self.is_match_data(match):
                prepared_match_data = {
                    'external_id': match[self.match_id],
                    'home_team': match[self.match_home],
                    'away_team': match[self.match_away],
                    'date': match[self.match_date],
                    'sport': sport_name,
                    'championship': championship_name,
                    'duplicates': self.get_duplicate_match(match),
                }
                self.parsed_data.append(prepared_match_data)

    def parse_championships(self, sport_name, championship_data):
        """парсинг данных чемпионатов"""
        for championship in championship_data:
            self.processing_match_data(
                sport_name,
                championship[self.championship_name],
                championship[self.matches]
            )

    def parse_sports(self, sport_data):
        """парсинг данных спорта"""
        for sport_type in sport_data[self.sport_types]:
            self.parse_championships(
                sport_type[self.sport_name],
                sport_type[self.championship_types]
            )

    def run(self):
        """запуск парсинга и возвращения результата"""
        try:
            for file in os.listdir(path=FILE_PATH['SPORT']):
                with open(FILE_PATH['SPORT']+file) as sport_json_data:
                    self.parse_sports(json.loads(sport_json_data.readline()))

            return self.parsed_data
        except json.JSONDecodeError:
            print('Не валидный json в файле '+file)
