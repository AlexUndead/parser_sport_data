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

    def is_variable_match(self, match):
        """проверка непосредственного исхода матча"""
        return True if match[self.event_type] == '' and match['A'] != 'Гости (голы)' else False

    def get_duplicate_match(self, match):
        """получение дубликаты матчей"""
        return [duplicate[self.match_id] for duplicate in match[self.matches]]

    def preparation_matches(self, sport_name, championship_name, matches):
        """подготовка матчей"""
        for match in matches:
            if self.is_variable_match(match):
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

    def preparation_championships(self, sport_name, championship_data):
        """подготовка чемпионатов"""
        for championship in championship_data:
            self.preparation_matches(
                sport_name,
                championship[self.championship_name],
                championship[self.matches]
            )

    def validate_data(self, sport_data):
        """обработка спортивных данных"""
        for sport_type in sport_data[self.sport_types]:
            self.preparation_championships(
                sport_type[self.sport_name],
                sport_type[self.championship_types]
            )

    def run(self):
        """запуск парсинга и возвращения результата"""
        for file in os.listdir(path=FILE_PATH['SPORT']):
            with open(FILE_PATH['SPORT']+file) as json_data:
                self.validate_data(json.loads(json_data.readline()))

        return self.parsed_data
