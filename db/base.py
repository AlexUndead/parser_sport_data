from config import DB_SETTINGS

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+mysqldb://' +
    DB_SETTINGS['USER'] +
    ':' +
    DB_SETTINGS['PASSWORD'] +
    '@' +
    DB_SETTINGS['HOST'] +
    ':' +
    DB_SETTINGS['PORT'] +
    '/' +
    DB_SETTINGS['NAME'] +
    '?charset=utf8mb4'
)
metadata = MetaData(bind=engine)
session = sessionmaker(bind=engine)


@as_declarative(metadata=metadata)
class Base:
    """Базовый класс работы с бд"""
    pass
