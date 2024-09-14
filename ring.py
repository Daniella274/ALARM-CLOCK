from pygame import mixer
from tkinter.ttk import *
from tkinter import *
from datetime import datetime       #work with date and time
from time import sleep

def Ring_alarm():
    mixer.music.load(r"C:\Users\Daniella\OneDrive\Desktop\Alarm Clock\loud_alarm_sound.mp3")
    mixer.music.play()
    
    
  # Creating a function for time.
def Alarm(): 
    while True: 
        control = 1
        print(control)
        alarm_hur = '18'
        alarm_min = '39'
        alarm_sec = '00' 
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
Alarm() 
    
clock.mainloop()