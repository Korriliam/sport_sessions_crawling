from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import sport_sessions_crawling.settings as settings

DeclarativeBase = declarative_base()

def connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_tables(engine):
    """
    Creating our tables
    """
    DeclarativeBase.metadata.create_all(engine)

def Event(DeclarativeBase):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    link = Column('link', String, nullable=True)
    location = Column('location', String, nullable=True)
    date = Column('date', DateTime, nullable=True)
    length = Column('length', Integer)

def Sport(DeclarativeBase):
    __tablename__ = "sport"

    id = Column(Integer, primary_key=True)

def Source(DeclarativeBase):
    __tablename__ = "source"

    id = Column(Integer, primary_key=True)


def Session(DeclarativeBase):
    __tablename__ = "session"

    id = Column(Integer, primary_key=True)


def Track(DeclarativeBase):
    __tablename__ = "track"

    id = Column(Integer, primary_key=True)