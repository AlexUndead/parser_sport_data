from sqlalchemy import ForeignKey, Column, Integer, String, DateTime
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


class Duplicate(Base):
    """таблица дубликатов матрей"""
    __tablename__ = 'duplicate'

    id = Column(Integer, primary_key=True)
    match = Column(Integer, ForeignKey('match.id'), nullable=False)
    duplicate_match_id = Column(String(50), unique=True)
