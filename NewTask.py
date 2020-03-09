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

    textSubject=Text(frameTask,width=20,heigh=2)
    textSubject.grid(row=1,column=0,padx=5,pady=5,sticky='w')

    root.mainloop()
if __name__ == '__NewTask__':
    NewTask()
