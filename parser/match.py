import json
from config import FILE_PATH
from db.receive import Receive


class Match:
    """Класс парсинга файлов видов матч"""
    event = 'Event'
    value = 'Value'
    block = 'B'
    coefficient = 'C'
    data_external_match_id = 'I'
    period = 'P'
    bet_name = 'S'
    bet_type = 'T'
    parsed_data = []

    def __init__(self):
        self.receive = Receive()

    def processing_match_bets_data(self, match_bets_data, external_match_id):
        """обработка данных о ставках матча"""
        for bet in match_bets_data:
            if not bet[self.block]:
                prepared_bet_data = {
                    'name': bet[self.bet_name],
                    'coefficient': bet[self.coefficient],
                    'match_external_id': bet[self.data_external_match_id],
                    'period': bet[self.period],
                    'type': bet[self.bet_type],
                    'match_id': self.receive.get_match_id_by_external_id(external_match_id),
                }
                self.parsed_data.append(prepared_bet_data)

    def parse_event(self, bet_data, external_match_id):
        """парсинг данных событий"""
        for event in bet_data[self.event]:
            self.processing_match_bets_data(
                event[self.value],
                external_match_id
            )

    def get_match_bets(self, external_match_id):
        """получение обработанной информации"""
        try:
            with open(FILE_PATH['MATCH']+external_match_id+'.json') as match_bets_json_data:
                self.parse_event(
                    json.loads(match_bets_json_data.readline()),
                    external_match_id,
                )

            return self.parsed_data
        except FileNotFoundError:
            print('Файл '+external_match_id+'.json не найден')
        except json.JSONDecodeError:
            print('Не валидный json в файле '+external_match_id+'.json')
