import xml.etree.ElementTree as ET
import sqlite3

create_Artist='''CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
); '''
create_Genre= '''CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);'''
create_Album='''CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);'''
create_Track='''CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);'''
def createSQL():
    cur.executescript(create_Artist)
    cur.executescript(create_Genre)
    cur.executescript(create_Album)
    cur.executescript(create_Track)

def getData(dicR):
    rd={"Artist":None,
    "Genre":None,
    "Album":None,
    "Name":None,
    "Total Time":None,
    "Rating":None,
    "Play Count":None}
    label=None
    for i in dicR:
        if i.text in rd:
            label=i.text
            continue
        if label:
            rd[label]=i.text
            label=None
    writable =rd["Genre"] is not None and rd["Name"] is not None and rd["Artist"] is not None and rd["Album"] is not None 
        
    return rd,writable


fname="tracks/Library.xml"
tree = ET.parse(fname)
root = tree.getroot()
elems=root.findall("dict/dict/dict")
total=len(elems)
c=1
conn = sqlite3.connect('homework6.sqlite')
cur = conn.cursor()
createSQL()
for elem in elems:
    data,writable=getData(elem)
    
    if not writable: continue

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( data["Artist"], ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (data["Artist"], ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( data["Genre"], ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (data["Genre"], ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( data["Album"], artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (data["Album"], ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count,genre_id) 
        VALUES ( ?, ?, ?, ?, ?,? )''', 
        ( data["Name"], album_id, data["Total Time"], data["Rating"], data["Play Count"],genre_id ) )
    print("Progress {}%".format(c*100/total))
    c+=1
    conn.commit()