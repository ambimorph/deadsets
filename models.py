from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    textfile = db.Column(db.String)
    date = db.Column(db.DateTime)
    city = db.Column(db.String)
    songs = db.relationship('Song', secondary='show_song')

class Song(db.Model):
    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    shows = db.relationship('Show', secondary='show_song')

class ShowSong(db.Model):
    __tablename__ = 'show_song'
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), primary_key=True)

"""

from models import *
import datetime
db.create_all()
s = db.session()
m = Song(title='Might As Well')
s.add(m)
s.commit()
oct = Show(textfile='10-10-76.txt', date=datetime.datetime(1976,10,10), city='Oakland')
oct.songs.append(m)
s.add(oct)
s.commit()
sept = Show(textfile='9-24-76.txt', date=datetime.datetime(1976,9,26), city='WilliamsIn [12]: 
sept.songs.append(m)
s.add(sept)
s.commit()
x = s.query(Song).filter(Song.title == 'Might As Well').one()
[y.textfile for y in x.shows]
Out: [u'10-10-76.txt', u'9-24-76.txt']

"""
