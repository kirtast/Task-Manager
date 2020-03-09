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
    root.resizable(0,0)
    frameTask=Frame(root)
    frameTask.grid(row=0,column=0,sticky=W+E)

    labelSubject=Label(frameTask,text='Subject:')
    labelSubject.grid(row=0,column=0,padx=5,pady=5,sticky='w')

    textSubject=Text(frameTask,width=50,heigh=1)
    textSubject.grid(row=1,column=0,padx=5,pady=5,sticky='w')

    labelDesc=Label(frameTask,text='Description:')
    labelDesc.grid(row=2,column=0,padx=5,pady=5,sticky='w')
    textSubject=Text(frameTask,width=75,heigh=5)
    textSubject.grid(row=3,column=0,padx=5,pady=5,sticky='w')
    def submit():
        a=1
        #acciones para meter esto en una sql
    botonSubmit=Button(frameTask,text='SUBMIT',command=submit)
    botonSubmit.grid(row=4,column=0,padx=5,pady=5,sticky='w')


    root.mainloop()
if __name__ == '__NewTask__':
    NewTask()
