#!python 3

import tkinter as tk
import playsound as p

def playsound(event):
    print(event)
    p.playsound("animals_dogs_x2_barking_small_001.mp3")


win = tk.Tk()
win.attributes('-topmost',True)
l1 = tk.Label(win,text="This button has an event bound by a command")
l2 = tk.Label(win,text="This button has an event bound by a bind")

# buttons b1 and b2 do the same
# note that the callback for b1 is included in its definition
# but the callback for b2 is in a separate command
b1 =  tk.Button(win,text="Click to play",command="playsound")
b2 =  tk.Button(win,text="Click to play")
b2.bind("<Button>",playsound)


l1.pack()
b1.pack()
l2.pack()
b2.pack()

win.mainloop()

