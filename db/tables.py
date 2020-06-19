from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from .base import Base, engine


class Sport(Base):
    """таблица спорта"""
    __tablename__ = 'sport'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    matches = relationship('Match', backref='sport')


class Championship(Base):
    """таблица чемпионатов"""
    __tablename__ = 'championship'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    matches = relationship('Match', backref='championship')


class Match(Base):
    """таблица матчей"""
    __tablename__ = 'match'

    id = Column(Integer, primary_key=True, autoincrement=True)
    external_id = Column(String(50), unique=True)
    home_team = Column(String(255))
    away_team = Column(String(255))
    date = Column(DateTime)
    sport_id = Column(Integer, ForeignKey('sport.id'), nullable=False)
    championship_id = Column(Integer, ForeignKey('championship.id'))
    duplicate = relationship('Duplicate', backref='duplicate')
    bet = relationship('Bet', backref='bet')


class Duplicate(Base):
    """таблица дубликатов матчей"""
    __tablename__ = 'duplicate'

    id = Column(Integer, primary_key=True)
    parent_match_id = Column(Integer, ForeignKey('match.id'), nullable=False)
    external_match_id = Column(String(50), unique=True)


class Bet(Base):
    """таблица ставок на матч"""
    __tablename__ = 'bet'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    coefficient = Column(Float)
    match_external_id = Column(String(50), nullable=True)
    period = Column(Float)
    type = Column(Integer)
    match_id = Column(Integer, ForeignKey('match.id'), nullable=False)
