from db.base import Base, engine, session
from db.tables import Sport, Championship, Match, Duplicate


class Receive:
    """Класс получение данных из бд"""

    def __init__(self):
        self.session = session()

    def get_all_ids_match(self, match_id):
        """получение всех id матча (с дубликатами)"""
        match = self.session.query(Match) \
            .filter_by(external_id=match_id).first()

        all_match_ids = [match.external_id]
        all_match_ids.extend([duplicate_id.duplicate_match_id for
                              duplicate_id in match.duplicate])

        return all_match_ids
