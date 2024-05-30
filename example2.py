#!python 3
# same program, better use of variables!
import tkinter as tk
import playsound as p

def playsound(event):
    print(event)
    p.playsound("animals_dogs_x2_barking_small_001.mp3")


win = tk.Tk()
win.attributes('-topmost',True)

l = []
l.append(tk.Label(win,text="This button has an event bound by a command"))
l.append(tk.Label(win,text="This button has an event bound by a bind"))

b = []
b.append(tk.Button(win,text="Click to play",command="playsound"))
b.append(tk.Button(win,text="Click to play"))
b[1].bind("<Button>",playsound)


for i in range(0,2):
    l[i].pack()
    b[i].pack()
    
win.mainloop()

