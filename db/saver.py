import re
import datetime
from db.base import Base, engine, session
from db.tables import Sport, Championship, Match, Duplicate


class Saver:
    """Класс для сохранения/изменения элементов бд"""
    def __init__(self, matches_data):
        self.matches = matches_data
        self.session = session()
        self.create_schema()

    def create_schema(self):
        """создать базу данных"""
        Base.metadata.create_all(engine)

    def get_sport_object(self, sport_name):
        """получить обект орм спорт"""
        sport = self.session.query(Sport)\
            .filter_by(name=sport_name).first()
        if sport is None:
            return Sport(name=sport_name)

        return sport

    def get_championship_object(self, championship_name):
        """получить обект орм чемпионат"""
        championship = self.session.query(Championship)\
            .filter_by(name=championship_name).first()
        if championship is None:
            return Championship(name=championship_name)

        return championship

    def change_match_object(self, match, match_data):
        """именение объекта орм матч"""
        match.external_id = match_data['external_id'],
        match.home_team = match_data['home_team'],
        match.away_team = match_data['away_team'],
        match.date = self.get_transform_date(match_data['date']),
        match.sport_id = self.get_sport_object(match_data['sport']).id,
        match.championship_id = self.get_championship_object(match_data['championship']).id,

        return match

    def get_duplicate_objects(self, duplicates):
        """получить массив объектов орм сущности дубликат матча"""
        return [Duplicate(duplicate_match_id=duplicate) for duplicate in duplicates]

    def get_transform_date(self, raw_match_date):
        """получить преобразованное время"""
        raw_date = re.search(r'\d{10}', raw_match_date)
        return datetime.datetime.fromtimestamp(int(raw_date.group(0))).strftime('%Y-%m-%d %H:%M:%S')

    def get_match_object(self, match_data):
        """получить новый или уже созданный обект орм матча"""
        match = self.session.query(Match) \
            .filter_by(external_id=match_data['external_id']).first()
        if match is None:
            return Match(
                external_id=match_data['external_id'],
                home_team=match_data['home_team'],
                away_team=match_data['away_team'],
                date=self.get_transform_date(match_data['date']),
                sport=self.get_sport_object(match_data['sport']),
                championship=self.get_championship_object(match_data['championship']),
                duplicate=self.get_duplicate_objects(match_data['duplicates'])
            )
        else:
            match = self.change_match_object(match, match_data)

        return match

    def save(self):
        """сохранение матчей и возвращение id сохраненных матчей"""
        match_after_save = []

        for match in self.matches:
            match = self.get_match_object(match)
            match_after_save.append(match)

            self.session.add(match)

        self.session.flush()
        self.session.commit()

        return [match.external_id for match in match_after_save]
