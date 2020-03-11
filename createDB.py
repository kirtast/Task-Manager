import sqlite3
import urllib.request, urllib.parse

conn=sqlite3.connect('DataBaseTM.sqlite')
cur=conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Tasks;
DROP TABLE IF EXISTS SubTasks;
DROP TABLE IF EXISTS State;
'''
)
cur.executescript('''
CREATE TABLE Tasks(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,Date_Planned DATE, Date_Started DATE, Task_Subject TEXT UNIQUE,Task_Description,Task_State INTEGER,Date_Task_End DATE);
CREATE TABLE SubTasks(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,Task_id INTEGER,Subtask_Subject TEXT, SubTask_Description);
CREATE TABLE State(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,State TEXT UNIQUE,Description TEXT UNIQUE);
'''
)

States=[(0,'NO ACTIVO'),(1,'ACTIVO')]

for val in States:
    cur.execute('INSERT OR IGNORE INTO State(State,Description) VALUES (?,?)',(val[0],val[1],))


conn.commit()
cur.close()
