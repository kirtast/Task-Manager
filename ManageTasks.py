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
    comboTasks=ttk.Combobox(frameMan,width=15,heigh=1)
    comboTasks.grid(row=1,column=0)

    labelDesc=Label(frameMan,text='Task Description:')
    labelDesc.grid(row=0,column=1,padx=5,pady=5,sticky='w')
    textDescription=Text(frameMan,width=75,heigh=3)
    textDescription.grid(row=1,column=1,padx=5,pady=5,sticky='w')

    labelSubTasks=Label(frameMan,text='SUB TASKS:')
    labelSubTasks.grid(row=2,column=0,padx=0,pady=5,sticky='w')
    comboSubTasks=ttk.Combobox(frameMan,width=15,heigh=1)
    comboSubTasks.grid(row=3,column=0)

    labelSubDesc=Label(frameMan,text='Sub Task Description :')
    labelSubDesc.grid(row=2,column=1,padx=5,pady=5,sticky='w')
    textSubDescription=Text(frameMan,width=75,heigh=3)
    textSubDescription.grid(row=3,column=1,padx=5,pady=5,sticky='w')

    frameHist=Frame(root)
    frameHist.grid(row=1,column=0,sticky=W+E)

    # ListHist=Listbox(frameHist,width=225,height=40,borderwidth=1)
    # ListHist.grid(row=4,column=0)
    # ListHist.insert('end',newnames)
    conn=sqlite3.connect('DataBaseTM.sqlite')
    cur=conn.cursor()

    TasksOrder='''SELECT Tasks.Task_Subject FROM Tasks'''
    Tasks=list()
    for row in cur.execute(TasksOrder):
        Tasks.append(row[0])

    comboTasks.set('')
    comboTasks['values']=Tasks

    def callback(eventObject):
        Task=comboTasks.get()
        TaskIdObj=cur.execute('SELECT id FROM Tasks WHERE Task_Subject = ?',(Task,))
        idTask=list()
        for row in TaskIdObj:
            idTask.append(row[0])
        DescIdObj=cur.execute('SELECT Task_Description FROM Tasks WHERE Task_Subject = ?',(Task,))
        DescTask=list()
        for row in DescIdObj:
            DescTask.append(row[0])
        textDescription.delete('1.0','end')
        textDescription.insert('end',DescTask[0])
        SubTaskIdObj=cur.execute('SELECT Subtask_Subject FROM SubTasks WHERE Task_id = ?',(idTask[0],))
        SubTasks=list()
        for row in SubTaskIdObj:
            SubTasks.append(row[0])
        comboSubTasks.set('')
        comboSubTasks['values']=SubTasks
    def callback2(eventObject):
        SubTask=comboSubTasks.get()
        Task=comboTasks.get()
        TaskIdObj=cur.execute('SELECT id FROM Tasks WHERE Task_Subject = ?',(Task,))
        idTask=list()
        for row in TaskIdObj:
            idTask.append(row[0])
        SubTaskIdObj=cur.execute('SELECT SubTask_Description FROM SubTasks WHERE Task_id = ? AND Subtask_Subject = ?',(idTask[0],SubTask,))
        SubTasksDesc=list()
        for row in SubTaskIdObj:
            SubTasksDesc.append(row[0])
        textSubDescription.delete('1.0','end')
        textSubDescription.insert('end',SubTasksDesc[0])



    comboTasks.bind("<<ComboboxSelected>>", callback)
    comboSubTasks.bind("<<ComboboxSelected>>", callback2)

    conn.commit()
    root.mainloop()
    cur.close()

if __name__ == '__ManageTasks__':
    ManageTasks()
