from db.base import Base, engine, session
from db.tables import Sport, Championship, Match, Duplicate


class Receive:
    """Класс получение данных из бд"""

    def __init__(self):
        self.session = session()

    def get_all_ids_match(self, external_match_id):
        """получение всех id матча (с дубликатами)"""
        match = self.session.query(Match) \
            .filter_by(external_id=external_match_id).first()

        all_match_ids = [match.external_id]
        all_match_ids.extend([duplicate_id.external_match_id for
                              duplicate_id in match.duplicate])

        return all_match_ids

    def get_match_id_by_external_id(self, external_match_id):
        """получить id матча по внешнему id"""
        match_id = self.session.query(Match.id).filter_by(external_id=external_match_id).first()
        if not match_id:
            match_id = self.session.query(Duplicate.parent_match_id).\
                filter_by(external_match_id=external_match_id).first()

        if match_id:
            match_id = match_id[0]

        return match_id
