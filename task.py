import tkinter as tk 
from tkinter import *
from tkinter import ttk




win = tk.Tk()
win.attributes('-topmost',True)
l1 = tk.Label(win,text="This button has an event bound by a command")
l2 = tk.Label(win,text="This button has an event bound by a bind")

# buttons b1 and b2 do the same
# note that the callback for b1 is included in its definition
# but the callback for b2 is in a separate command
Lion =  tk.Button(win,text="Click to play",command="lion.mp3") 
snake =  tk.Button(win,text="Click to play",command="snake.mp3")
Pig =  tk.Button(win,text="Click to play",command="oink.mp3")
Bear =  tk.Button(win,text="Click to play",command="")
Yipee=  tk.Button(win,text="Click to play",command="")

Lion.bind("<Button>")


l1.pack()
l2.pack()

Lion.pack()
snake.pack()
Pig.pack()
Bear.pack()
Yipee.pack()


win.mainloop()