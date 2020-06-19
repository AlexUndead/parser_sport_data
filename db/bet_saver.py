from db.base import session
from db.tables import Bet


class BetSaver:
    """класс для сохранения ставок"""
    def __init__(self):
        self.session = session()

    def change_bet_object(self, bet, bet_data):
        """именение объекта орм ставки"""
        bet.name = bet_data['name'],
        bet.coefficient = bet_data['coefficient'],
        bet.match_external_id = bet_data['match_external_id']
        bet.period = bet_data['period']
        bet.type = bet_data['type']
        bet.match_id = bet_data['match_id']

        return bet

    def get_bet_object(self, bet_data):
        """получить новый или уже созданный обект орм ставки"""
        bet = self.session.query(Bet) \
            .filter_by(
            match_id=bet_data['match_id'],
            name=bet_data['name'],
        ).first()
        if bet is None:
            return Bet(
                name=bet_data['name'],
                coefficient=float(bet_data['coefficient']),
                match_external_id=bet_data['match_external_id'],
                period=float(bet_data['period']),
                type=int(bet_data['type']),
                match_id=bet_data['match_id'],
            )
        else:
            bet = self.change_bet_object(bet, bet_data)

        return bet

    def save(self, bet_data):
        """сохранение ставок матчей"""
        bets_objects = []
        for bet in bet_data:
            bets_objects.append(self.get_bet_object(bet))

        self.session.add_all(bets_objects)
        self.session.flush()
        self.session.commit()
