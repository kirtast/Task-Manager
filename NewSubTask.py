from tkinter import *
import tkinter.ttk as ttk
import datetime
import sqlite3
import urllib.request, urllib.parse
import datetime
from pandas import DataFrame
import pandas as pd
from tkcalendar import Calendar, DateEntry

def NewSubTask():
    root=Tk()
    root.title('NEW SUB TASK')
    root.resizable(0,0)
    frameSubTask=Frame(root)
    frameSubTask.grid(row=0,column=0,sticky=W+E)

    labelSubject=Label(frameSubTask,text='Task:')
    labelSubject.grid(row=0,column=0,padx=5,pady=5,sticky='w')

    comboTask=ttk.Combobox(frameSubTask)
    comboTask.grid(row=1,column=0,padx=5,pady=5,sticky='w')

    labelSubject=Label(frameSubTask,text='Subject:')
    labelSubject.grid(row=2,column=0,padx=5,pady=5,sticky='w')
    textSubject=Text(frameSubTask,width=50,heigh=1)
    textSubject.grid(row=3,column=0,padx=5,pady=5,sticky='w')

    labelDesc=Label(frameSubTask,text='Description:')
    labelDesc.grid(row=4,column=0,padx=5,pady=5,sticky='w')
    textDescription=Text(frameSubTask,width=75,heigh=5)
    textDescription.grid(row=5,column=0,padx=5,pady=5,sticky='w')

    conn=sqlite3.connect('DataBaseTM.sqlite')
    cur=conn.cursor()

    TasksOrder='''SELECT Tasks.Task_Subject FROM Tasks'''
    Tasks=list()
    for row in cur.execute(TasksOrder):
        Tasks.append(row[0])

    comboTask.set('')
    comboTask['values']=Tasks
    def submitSubTask():
        subTasksubject=textSubject.get('1.0','end')
        subTaskdescription=textDescription.get('1.0','end')
        Task=comboTask.get()
        TaskIdObj=cur.execute('SELECT id FROM Tasks WHERE Task_Subject = ?',(Task,))
        for id in TaskIdObj:
            TaskId=id[0]
        cur.execute('INSERT OR IGNORE INTO SubTasks(Task_id,Subtask_Subject,Subtask_Description) VALUES (?,?,?)',(TaskId,subTasksubject,subTaskdescription,))
        conn.commit()
    botonSubmit=Button(frameSubTask,text='SUBMIT',command=submitSubTask)
    botonSubmit.grid(row=6,column=0,padx=5,pady=5,sticky='w')

    conn.commit()
    root.mainloop()
    cur.close()
if __name__ == '__NewSubTask__':
    NewSubTask()
