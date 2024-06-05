import tkinter as tk 
from tkinter import *
from tkinter import ttk
import playsound as p


def playsound(event):
    print(event)
    p.playsound("Bear.mp3")

def playsound2(event2):
    print(event2)
    p.playsound("lion.mp3")

def playsound3(event3):
    print(event3)
    p.playsound("oink.mp3")

def playsound4(event4):
    print(event4)
    p.playsound("snake.mp3")

def playsound5(event5):
    print(event5)
    p.playsound("yipee.mp3")

win = tk.Tk()
win.attributes('-topmost',True)
l1 = tk.Label(win,text="This button has an event bound by a command")
l2 = tk.Label(win,text="This button has an event bound by a bind")

# buttons b1 and b2 do the same
# note that the callback for b1 is included in its definition
# but the callback for b2 is in a separate command
Lion =  tk.Button(win,text="Click to play",command="playsound2") 
snake =  tk.Button(win,text="Click to play",command="playsound4")
Pig =  tk.Button(win,text="Click to play",command="playsound3")
Bear =  tk.Button(win,text="Click to play",command="playsound")
Yipee=  tk.Button(win,text="Click to play",command="playsound5")

playsound
Lion.bind("<Button>")




Lion.grid(row = 5, column = 5)
snake.grid()



win.mainloop()