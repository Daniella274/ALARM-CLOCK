from tkinter.ttk import *
from tkinter import *
from datetime import datetime
import time
from time import sleep
import time
from PIL import ImageTk, Image
from threading import Thread
from pygame import mixer
from time import sleep

Clock = Tk()
Clock.title("Daniella's Clock")
Clock.geometry("650x400")
Clock.configure(bg = "White")

Clock_Frame = Frame (Clock , width= 450, height=5, bg= "teal")
Clock_Frame.grid(row=0 , column= 0)

Bodyof_Frame = Frame (Clock , width=650, height=400, bg= "white")
Bodyof_Frame.grid (row = 1, column=0)
Picture = Image.open(r"C:\Users\Daniella\OneDrive\Desktop\Alarm Clock\Alarm image 2.webp")
Picture.resize ((150,150))
Picture = ImageTk.PhotoImage(Picture)
Photo = Label(Bodyof_Frame, height=325,image=Picture, bg= "white")
Photo.place(x = 10, y = 10)

#Input of Variables
time_format=Label(Bodyof_Frame, text= "Time in 24hrs format!", fg="black",bg="white",font="Timeroman 18 bold", height=1).place(x=380,y=280)
setYourAlarm = Label(Bodyof_Frame,text = "Wake up time!",fg="black",relief = "solid",font=("Timeroman 15 bold")).place(x=150, y=155)


#setting the width and height of the time:
hour= Label(Bodyof_Frame,text = 'hour',bg = "white",width = 5, font=('timeroman 15 bold')).place(x=420,y=100)
c_hour = Combobox(Bodyof_Frame, width=2, font=('timeroman 15 bold'))
c_hour['values'] = ('00','01','02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19','20','21','22','23','24')
c_hour.current(0)
c_hour.place(x=430, y=130)

#Minutes
min= Label(Bodyof_Frame,text = 'min',bg = "white",width = 5, font=('timeroman 15 bold')).place(x=480,y=100)
c_min = Combobox(Bodyof_Frame, width=2, font=('timeroman 15 bold'))
c_min['values'] = ('00','01','02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19','20','21','22','23','24', '25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
c_min.current(0)
c_min.place(x=490, y=130)
#Seconds 
sec = Label(Bodyof_Frame,text = 'sec',bg = "white",width = 5, font=('timeroman 15 bold')).place(x=540,y=100)
c_sec = Combobox(Bodyof_Frame, width=2, font=('timeroman 15 bold'))
c_sec['values'] = ('00','01','02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19','20','21','22','23','24', '25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
c_sec.current(0)
c_sec.place(x=550, y=130)

#Function to activate alarm
def activate_alarm():
    t = Thread(target=Alarm)
    t.start()
    
#Activation button
selected = IntVar()
radio_bu = Radiobutton(Bodyof_Frame, font=('timeroman', 12, 'bold'), value=1, text='Activate', bg='white', variable=selected, command=activate_alarm)
radio_bu.place(x=410, y=230)
#Function to deactivate alarm
def Deactivate_alarm():
    print('Deactived alarm: ', selected.get())
    mixer.music.stop()   
   
def Ring_alarm():
    mixer.music.load(r"C:\Users\Daniella\OneDrive\Desktop\Alarm Clock\loud_alarm_sound.mp3")
    mixer.music.play()
    selected.set(0)
 #Deactivation button
    radio_bu_2 = Radiobutton(Bodyof_Frame, font=('timeroman', 10, 'bold'), value=2, text='Deactivate', bg='white', variable=selected, command=Deactivate_alarm)
    radio_bu_2.place(x=520, y=230)

# Creating a function for time.
def Alarm(): 
    while True: 
        control = selected.get()
        print(control)
        alarm_hur = c_hour.get()
        alarm_min = c_min.get()
        alarm_sec = c_sec.get()
        current_time = datetime.now() 
        hour = current_time.strftime("%H")
        min = current_time.strftime("%M") 
        sec = current_time.strftime("%S")
    
        if control ==1:
            if alarm_hur == hour:
                if alarm_min == min:
                    if alarm_sec == sec:
                        print("The time is now!")
                        Ring_alarm() 
        sleep(1)


mixer.init()

Clock.mainloop()