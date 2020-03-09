

from tkinter import *
import tkinter.ttk as ttk
import datetime
import sqlite3
import urllib.request, urllib.parse
import datetime
from pandas import DataFrame
import pandas as pd
from tkcalendar import Calendar, DateEntry

from NewTask import*


def main():
    root=Tk()
    root.title('TASK MENU')

    root.resizable(0,0)
    #root.iconbitmap('seat_logo.ico')

    frameMain=Frame(root)
    frameMain.grid(row=0,column=0,sticky=W+E)
    labelBotonMainTask=Label(frameMain,text='New Task:')
    labelBotonMainTask.grid(row=0,column=0,padx=5,pady=5,sticky='w')
    def openNewTask():
        NewTask()
    botonNewTask=Button(frameMain,text='NEW TASK',command=openNewTask())
    # botonNewTask=Button(frameMain,text='NEW TASK')
    botonNewTask.grid(row=1,column=0,padx=5,pady=5,sticky='w')




    root.mainloop()




if __name__ == '__main__':
    main()
