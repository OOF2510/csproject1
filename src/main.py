"""
Author: Nathan Turner
Created: 10/18/22
Version: 1.0.2
"""

# imports
from tkinter import *
from tkinter import ttk
from pynput.mouse import Button, Controller
from pynput import keyboard
from time import sleep as wait

# make a new mouse controller named mouse_control
mouse_control = Controller()

# function to add a range of numbers to a list
def add_range(list, amount):
    for i in range(amount):
        list.append(i)

# create seconds list and add seconds 0-25 to it
seconds = []
add_range(seconds, 26)
mouse_buttons = ["Left Click", "Left Click", "Middle Click", "Right Click"] # list of options for the mouse button dropdown
# map options to thier respective buttons
buttonmap = {
    "Left Click": Button.left,
    "Middle Click": Button.middle,
    "Right Click": Button.right
}

# if esc is pressed, set endkey_pressed to True
endkey_pressed = False
def on_release(key):
    if key == keyboard.Key.esc:
        global endkey_pressed
        endkey_pressed = True
listener = keyboard.Listener(on_release=on_release)
listener.start()

# autoclicker function
def autoclick(sec, mb):
    mb = buttonmap[mb] # get the actual button from user selection
    sec = int(sec) # make sec a int
    global running
    global endkey_pressed
    running = True
    endkey_pressed = False
    print(f"Autoclicker started, press the 'esc' key twice to end") # instructions to end
    while running: # repeat while running is True
        # press then release mouse button
        mouse_control.press(mb)
        mouse_control.release(mb)
        # if endkey has been pressed, set running to false, else, wait user specified amount of seconds
        if endkey_pressed == True:   
            running = False
        else:
            wait(sec)
    print("Stopped")

# initialize window using tkinter
win = Tk()
win.title("Autoclicker")
win.geometry('600x200')

label = ttk.Label(win, text="Seconds in between clicks:")
label.place(x=20,y=10,width=190,height=25)

# create dropdown menu from the seconds list
time_choice = StringVar(win)
time_choice.set(seconds[1])
time_dropdown = ttk.OptionMenu(win, time_choice, *seconds)
time_dropdown.place(x=230,y=10,width=70,height=25)

label = ttk.Label(win, text="Mouse button to click:")
label.place(x=20,y=40,width=190,height=25)

# create dropdown menu from the mouse_buttons list
mb_choice = StringVar(win)
mb_choice.set(mouse_buttons[1])
mb_dropdown = ttk.OptionMenu(win, mb_choice, *mouse_buttons)
mb_dropdown.place(x=230,y=40,width=130,height=25)

# wrapper function for autoclick since tk callback doesnt allow passing paramaters
def autoclick_wrapper:
  autoclick(time_choice.get(), mb_choparamaters # run autoclick function, passing user selected options as params
# create start button which runs the autoclick_wrapper function
start_button = ttk.Button(win, text="Start", command=autoclick_wrapper)
start_button.place(x=200,y=170,width=70,height=25)

# create quit button
quit_button = ttk.Button(win, text="Quit", command=win.destroy)
quit_button.place(x=300,y=170,width=70,height=25)

win.mainloop() # run the window
