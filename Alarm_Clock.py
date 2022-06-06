#!/usr/bin/python3
# This project is focused on creating an alarm clock

import datetime
import time
import winsound
from tkinter import *
from tkinter import messagebox
from threading import Thread

def Alarm(set_alarm_timer):

    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%m/%d/%Y")
        #print("The Set Date is:",date)
        #print(now)
        if now == set_alarm_timer:
            messagebox.showinfo(title="Alarm",message="Time to wake up")
            winsound.PlaySound("sound.wav",winsound.SND_LOOP)
            break
        #print(storeArray);
           


def actual_time():
    set_alarm_timer = f'{hour.get()}:{min.get()}:{sec.get()}'
    new_thread=Thread(target=Alarm,args=(set_alarm_timer,))
    new_thread.daemon=True
    new_thread.start()

#----------------------------------------------------GUI for the user------------------------------------------------------------------------------- 
clock = Tk()
clock.title("Alarm Clock")
clock.geometry("350x280")
storeArray=[]
def Alarm(set_alarm_timer):

    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%m/%d/%Y")
        #print("The Set Date is:",date)
        #print(now)
        if now == set_alarm_timer:
            
            winsound.PlaySound("sound.wav",winsound.SND_LOOP)
            break
        #print(storeArray);
           


def actual_time(storeArray):
    set_alarm_timer = f'{hour.get()}:{min.get()}:{sec.get()}'
    storeArray.append(set_alarm_timer)
    new_thread=Thread(target=Alarm,args=(set_alarm_timer,))
    new_thread.daemon=True
    new_thread.start()
    return storeArray


time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="white",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",9,"bold")).place(x=0, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(clock,bg = "pink",textvariable=hour,width = 15).place(x=125,y=30)
minTime= Entry(clock,bg = "pink", textvariable=min,width = 15).place(x=170,y=30)
secTime = Entry(clock,bg = "pink",textvariable=sec,width = 15).place(x=220,y=30)


submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time(storeArray)).place(x =110,y=70)

def alarmHistory():
    alarmTime=actual_time(storeArray)
    item=StringVar(value=alarmTime)
    alarmHistory=Listbox(clock,height=8,width=20,listvariable=item,selectmode='extended').place(x=260,y=90)
    scrollbar=Scrollbar(clock,orient='vertical',command=alarmHistory)
    return alarmHistory

def delete_alarm(alarmHistory):
    selected_index=alarmHistory.curseselection()
    selected_item=join([alarmHistory.get(i) for i in selected_index])
    answer=askokcancel(title='Deletion',message='Are you sure you want to delete selected items!')
    if answer:
        alarmHistory.delete(selected_item)
        showinfo(title='Deletion status',message='Alarm deleted')

  

historyButton = Button(clock, text="View Alarm history",command=alarmHistory,borderwidth=3,relief="groove").place(x=110,y=200)
clock.mainloop()     