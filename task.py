import tkinter as tk
from tkinter import PhotoImage
from playsound import playsound

def play_bear_sound(event=None):
    playsound("Bear.mp3", block=False)

def play_lion_sound(event=None):
    playsound("lion.mp3", block=False)

def play_oink_sound(event=None):
    playsound("oink.mp3", block=False)

def play_snake_sound(event=None):
    playsound("snake.mp3", block=False)

def play_yipee_sound(event=None):
    playsound("yipee.mp3", block=False)


win = tk.Tk()
win.title("Animal Soundboard")
win.attributes('-topmost', True)


labels = ["Bear", "Lion", "Pig", "Snake", "Yipee"]
callbacks = [play_bear_sound, play_lion_sound, play_oink_sound, play_snake_sound, play_yipee_sound]
buttons = []


bear_img = PhotoImage(file="bear.png")
lion_img = PhotoImage(file="lion.png")
pig_img = PhotoImage(file="pig.png")
snake_img = PhotoImage(file="snake.png")
yipee_img = PhotoImage(file="yipee.png")

images = [bear_img, lion_img, pig_img, snake_img, yipee_img]

for i, label in enumerate(labels):
    l = tk.Label(win, text=f"Click to play {label} sound")
    l.pack()
    b = tk.Button(win, text=f"Play {label} Sound", image=images[i], compound="left")
    b.bind("<Button>", callbacks[i])
    b.pack()
    buttons.append(b)


win.mainloop()
