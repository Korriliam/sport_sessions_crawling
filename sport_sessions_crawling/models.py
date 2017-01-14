from contextlib import contextmanager
from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import sport_sessions_crawling.settings as settings

DeclarativeBase = declarative_base()

class db(object):
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    __shared_state = {}

    def __init__ (self):
        self.__dict__ = self.__shared_state
        if not hasattr(self, 'engine'):
            self.engine = create_engine(URL(**settings.DATABASE))
        if not hasattr(self, 'Session'):
            self.session = sessionmaker(bind=self.engine)()


def create_tables(engine):
    """
    Creating our tables if they're not included in database
    """
    DeclarativeBase.metadata.create_all(engine)

class Session(DeclarativeBase):
    __tablename__ = 'Session'

    id = Column(Integer, primary_key=True)
    energy = Column('energy', Integer)
    average_speed = Column('average_speed', Float)
    duration = Column('duration', Time)
    date = Column('date', DateTime)
    comment = Column('comment', String)
    average_heatrate = Column('average_heartrate', Integer)
    max_heartrate = Column('max_heartrate', Integer)
    id_track = Column(Integer, ForeignKey('track.id'))
    id_source = Column(Integer, ForeignKey('source.id'))
    id_sport = Column(Integer, ForeignKey('sport.id'))
    id_event = Column(Integer, ForeignKey('event.id'))
    id_user = Column(Integer, ForeignKey('user.id'))


class Event(DeclarativeBase):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    link = Column('link', String, nullable=True)
    location = Column('location', String, nullable=True)
    date = Column('date', DateTime, nullable=True)
    length = Column('length', Integer)
    session = relationship('Session', backref="event")

class Sport(DeclarativeBase):
    __tablename__ = "sport"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    session = relationship('Session', backref="sport")

class Source(DeclarativeBase):
    __tablename__ = "source"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    url = Column('url', String)
    session = relationship('Session', backref="source")

class Track(DeclarativeBase):
    __tablename__ = "track"

    id = Column(Integer, primary_key=True)
    filetype = Column('filetype', String)
    elevation = Column('elevation', Integer)
    distance = Column('distance', Float)
    content = Column('content', Binary)
    session = relationship('Session', backref="track")

class User(DeclarativeBase):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    age = Column('age', Integer)

    session = relationship('Session', backref='user')
