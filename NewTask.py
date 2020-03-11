from tkinter import *
import tkinter.ttk as ttk
import datetime
import sqlite3
import urllib.request, urllib.parse
import datetime
from pandas import DataFrame
import pandas as pd
from tkcalendar import Calendar, DateEntry

def NewTask():
    root=Tk()
    root.title('NEW TASK')

    conn=sqlite3.connect('DataBaseTM.sqlite')
    cur=conn.cursor()

    root.resizable(0,0)
    frameTask=Frame(root)
    frameTask.grid(row=0,column=0,sticky=W+E)

    labelSubject=Label(frameTask,text='Subject:')
    labelSubject.grid(row=0,column=0,padx=5,pady=5,sticky='w')
    textSubject=Text(frameTask,width=50,heigh=1)
    textSubject.grid(row=1,column=0,padx=5,pady=5,sticky='w')

    labelDesc=Label(frameTask,text='Description:')
    labelDesc.grid(row=2,column=0,padx=5,pady=5,sticky='w')
    textDescription=Text(frameTask,width=75,heigh=5)
    textDescription.grid(row=3,column=0,padx=5,pady=5,sticky='w')

    def submit():
        current_time_class = datetime.datetime.now()

        current_time=str(current_time_class.day)+ '/'+ str(current_time_class.month)+ '/' + str(current_time_class.year)
        tasksubject=textSubject.get('1.0','end')
        taskdescription=textDescription.get('1.0','end')
        state_obj=cur.execute('SELECT id FROM State WHERE Description = ?',('NO ACTIVO',))
        for a in state_obj:
            state=a[0]
        # print([current_time,'',tasksubject,taskdescription,state,''])
        cur.execute('INSERT OR IGNORE INTO Tasks(Date_Planned,Date_Started,Task_Subject,Task_Description,Task_State,Date_Task_End) VALUES (?,?,?,?,?,?)',(current_time,'',tasksubject,taskdescription,state,''))
        conn.commit()
    botonSubmit=Button(frameTask,text='SUBMIT',command=submit)
    botonSubmit.grid(row=4,column=0,padx=5,pady=5,sticky='w')


    root.mainloop()
if __name__ == '__NewTask__':
    NewTask()
