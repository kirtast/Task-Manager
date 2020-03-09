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

    root.mainloop()
if __name__ == '__NewSubTask__':
    NewSubTask()
