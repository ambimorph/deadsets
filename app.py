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

"""

from app import *
import datetime
s = session()
might = Song(title='Might As Well')
s.add(might)
oct = Show(textfile='10-10-76.txt', date=datetime.datetime(1976,10,10), city='Oakland')
oct.songs.append(might)
s.add(oct)
s.commit()
x = s.query(Song).filter(Song.title == 'Might As Well').all()
[y.shows for y in x]
[y.city for y in x.shows]
[y.textfile for y in x.shows]
sept = Show(textfile='9-24-76.txt', date=datetime.datetime(1976,9,26), city='Williamsburg')
sept.songs.append(might)
s.add(sept)
s.commit()
x = s.query(Song).filter(Song.title == 'Might As Well').one()
[y.textfile for y in x.shows]
[a.textfile for a in y]

"""
