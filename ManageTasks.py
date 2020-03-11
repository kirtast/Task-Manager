from tkinter import *
import tkinter.ttk as ttk
import datetime
import sqlite3
import urllib.request, urllib.parse
import datetime
from pandas import DataFrame
import pandas as pd
from tkcalendar import Calendar, DateEntry

def ManageTasks():
    root=Tk()
    root.title('MANAGE TASKS')
    root.resizable(1,1)
    frameMan=Frame(root)
    frameMan.grid(row=0,column=0,sticky=W+E)

    labelTasks=Label(frameMan,text='TASKS:')
    labelTasks.grid(row=0,column=0,padx=0,pady=5,sticky='w')
    comboTasks=ttk.Combobox(frameMan,width=3,heigh=1)
    comboTasks.grid(row=1,column=0)

    labelSubTasks=Label(frameMan,text='SUB TASKS:')
    labelSubTasks.grid(row=2,column=0,padx=0,pady=5,sticky='w')
    comboSubTasks=ttk.Combobox(frameMan,width=3,heigh=1)
    comboSubTasks.grid(row=3,column=0)

    frameHist=Frame(root)
    frameHist.grid(row=1,column=0,sticky=W+E)

    ListHist=Listbox(frameHist,width=225,height=40,borderwidth=1)
    ListHist.grid(row=4,column=0)
    # ListHist.insert('end',newnames)

    root.mainloop()
if __name__ == '__ManageTasks__':
    ManageTasks()
