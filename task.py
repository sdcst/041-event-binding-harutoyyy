import tkinter as tk
from tkinter import PhotoImage
import playsound as playsound


def play_Bear_sound(event=None):
    playsound("Bear.mp3", block=False)

def play_lion_sound(event=None):
    playsound("lion.mp3", block=False)

def play_oink_sound(event=None):
    playsound("oink", block=False)

def play_snake_sound(event=None):
    playsound("snake.mp3", block=False)

def play_yipee_sound(event=None):
    playsound("yipee.mp3", block=False)

# Initialize the main window
win = tk.Tk()
win.title("Animal Soundboard")
win.attributes('-topmost', True)

# Create labels and buttons for each sound
labels = ["Dog", "Cat", "Cow"]
callbacks = [play_dog_sound, play_cat_sound, play_cow_sound]
buttons = []

# Load images
dog_img = PhotoImage(file="dog.png")
cat_img = PhotoImage(file="cat.png")
cow_img = PhotoImage(file="cow.png")
images = [dog_img, cat_img, cow_img]

for i, label in enumerate(labels):
    l = tk.Label(win, text=f"Click to play {label} sound")
    l.pack()
    b = tk.Button(win, text=f"Play {label} Sound", image=images[i], compound="left")
    b.bind("<Button>", callbacks[i])
    b.pack()
    buttons.append(b)

# Run the Tkinter main loop
win.mainloop()
