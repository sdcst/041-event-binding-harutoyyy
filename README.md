## SDSS Computing Studies Python Assignment
### Sound Effects

Objectives:
* Add an event to a button using the command option or the bind command
* Adding sound effects to a TKinter GUI

A GUI is supposed to make input and output easier for the user, so
we had better learn how to send and receive data from some of the
widgets.

Today, we will be looking at creating our first event driven programs
that use the command option for button widgets.  This allows us to have
the program execute specific code when the button is clicked.  

Code is placed in a function called _Callback Function_.  It behaves much like a regular function, but is run specifically from an event, so the first input parameter is to retrieve information specifically about the event that triggered it.

Today we will be adding sound effects can also be added to the callback functions that are created and bound to events.  These can be easily incorporated using a module and playing mp3 sound files.

We will need to install the *playsound* module
Unfortunately, the latest version of Playsound (1.3.0) doesn't work very well, so we will need to load an *older* version, version 1.2.2
```
pip install playsound==1.2.2
```

Once the module is installed, it can be used in python:
```
import playsound

playsound.playsound("file.mp3")
```
or
```
from playsound import playsound

playsound("file.mp3")
```

Playsound files are *blocking*, which means that the first sound needs to finish playing before the next one begins.  If you want to make the playing asynchronous (sounds play regardless of whether the previous one is complete) we need to add an additional parameter:

```
playsound("file.mp3",block=False)
```


### 2 Tasks

##### Task 1
Create a sound board.
This is a collection of buttons that is each bound to a sound effect.  These are great ways to help teach little children the different sounds that animals make, especially if you can add an image of the animal to the button.
You can choose what sound effects to include in your sound board.  Early sound boards were just sampled music bound to electronic keyboards: https://www.youtube.com/watch?v=z0PJnc8BFTk

