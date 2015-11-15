from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Show(Base):
    __tablename__ = 'show'
    id = Column(Integer, primary_key=True)
    textfile = Column(String)
    date = Column(DateTime)
    city = Column(String)
    songs = relationship('Song', secondary='show_song')

class Song(Base):
    __tablename__ = 'song'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    shows = relationship('Show', secondary='show_song')

class ShowSong(Base):
    __tablename__ = 'show_song'
    show_id = Column(Integer, ForeignKey('show.id'), primary_key=True)
    song_id = Column(Integer, ForeignKey('song.id'), primary_key=True)

from sqlalchemy import create_engine
engine = create_engine('sqlite:///gds.db')

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
