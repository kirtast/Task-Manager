

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
from NewSubTask import*

def main():
    root=Tk()
    root.title('TASK MENU')

    root.resizable(1,1)
    #root.iconbitmap('seat_logo.ico')

    frameMain=Frame(root)
    frameMain.grid(row=0,column=0,sticky=W+E)
    labelbotonNewTask=Label(frameMain,text='New Task:')
    labelbotonNewTask.grid(row=0,column=0,padx=5,pady=5,sticky='w')
    def openNewTask():
        NewTask()
    botonNewTask=Button(frameMain,text='NEW TASK',command=openNewTask)
    # botonNewTask=Button(frameMain,text='NEW TASK')
    botonNewTask.grid(row=1,column=0,padx=5,pady=5,sticky='w')
    def openNewSubTask():
        NewSubTask()
    labelBotonNewSubTask=Label(frameMain,text='New Sub Task:')
    labelBotonNewSubTask.grid(row=2,column=0,padx=5,pady=5,sticky='w')
    botonNewSubTask=Button(frameMain,text='NEW SUB TASK',command=openNewSubTask)
    # botonNewTask=Button(frameMain,text='NEW TASK')
    botonNewSubTask.grid(row=3,column=0,padx=5,pady=5,sticky='w')

    root.mainloop()




if __name__ == '__main__':
    main()
