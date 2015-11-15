from models import *
import datetime
import os
from dateutil.parser import parse

db.create_all()
s = db.session()

def remove_trailers(s):
    return s.strip().rstrip('->').strip().rstrip('*').strip()

def parse_show_file(filename):
    f = open(filename, 'r')
    first_line = f.readline()
    city = first_line.split(',')[1].strip()
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
        date = parse(os.path.splitext(fname)[0])
        city, songs = parse_show_file(os.path.join(dirname,fname))
        sh = Show(textfile=fname, date=date, city=city)
        for title in songs:
            so = Song(title=title)
            s.add(so)
            sh.songs.append(so)
        s.add(sh)
        s.commit()
    #s.commit()  Should be here, but will commit at each step for testing

if __name__ == '__main__':
    
    import sys
    directory = sys.argv[1]
    load_files(directory)
            

"""
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
"""
