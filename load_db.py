from models import *
import datetime
import os
from dateutil.parser import parse

db.create_all()
s = db.session()

def remove_trailers(s):
    return s.strip().rstrip('->').strip().rstrip('*').strip()

def process_file(filename):
    city, songs = parse_show_file(filename)
    date = parse(os.path.splitext(os.path.basename(filename))[0])
    sh = Show(textfile=filename, date=date, city=city)
    for title in songs:
        so = Song(title=title)
        s.add(so)
        sh.songs.append(so)
    s.add(sh)
    s.commit()


def parse_show_file(filename):
    f = open(filename, 'r')
    first_line = f.readline()
    try:
        city = first_line.split(',')[1].strip()
    except IndexError, e:
        city = ''
    songs = []
    for line in f:
        if line.startswith('*'):
            break
        if line != '\n':
            title = remove_trailers(line)
            if title.startswith('E:'):
                title = title[3:]
            songs.append(title)
    return city, songs

def load_files(dirname):

    for fname in os.listdir(dirname):
        process_file(os.path.join(dirname, fname))

if __name__ == '__main__':

    import sys
    directory = sys.argv[1]
    load_files(directory)


"""

One at a time:
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


After db is loaded:
q = s.query(Song).filter(Song.title == 'Deal').all()
[y[0].textfile for y in [x.shows for x in q]]

"""
