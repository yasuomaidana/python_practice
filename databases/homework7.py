import json
import sqlite3


create_user='''CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);'''
create_course='''CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);'''
create_member='''CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);'''
clean_table='''DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;'''
# Do some setup
def create_Table():
    cur.executescript(clean_table)
    cur.executescript(create_user)
    cur.executescript(create_course)
    cur.executescript(create_member)


fname = 'roster_data.json'
str_data = open(fname).read()
json_data = json.loads(str_data)

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()
create_Table()
total=len(json_data)
c=0
for entry in json_data:

    name = entry[0]
    title = entry[1]
    role= entry[2]
    print((name, title))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id,role) VALUES ( ?, ?, ?)''',
        ( user_id, course_id,role ) )
    c+=1
    print("Percentage done: {}%".format(c*100/total))
    conn.commit()