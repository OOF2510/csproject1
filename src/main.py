"""
Author: Nathan Turner
Created: 10/18/22
Last Updated: 10/26/22
Version: 1.0.4
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
    amount = (amount * 10) + 1
    # add numbers to list, starting at 0 and ending at amount, with a step of .1
    for i in range(0, amount, 1):
        list.append(i/10)

# create seconds list and add seconds to it
seconds = []
add_range(seconds, 2)
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
        # reset run 2.1 seconds after autoclicker stops, this is the only way i could stop the autoclicker from running multiple times at once
        global run
        if run > 0:
            wait(2.1)
            run = 0
            print('You may start the autoclicker again now')
        else:
            pass
        # please god work... LETSGOOOOOOO IT WORKED
listener = keyboard.Listener(on_release=on_release)
listener.start()

run = 0 # initalize run as 0
# autoclicker function
def autoclick(sec, mb):
    global run
    if run > 0: # if run is greater than 0
        return # stop execution of function 
    run += 1
    mb = buttonmap[mb] # get the actual button from user selection
    sec = float(sec) # convert sec to float
    global running # make running a global variable
    global endkey_pressed # make endkey_pressed a global variable
    running = True # set running to True
    endkey_pressed = False # set endkey_pressed to False
    print(f"Autoclicker started, press the 'esc' key to end") # instructions to end
    while running: # repeat while running is True
        # press then release mouse button
        mouse_control.press(mb)
        mouse_control.release(mb)
        if endkey_pressed == True: # if endkey has been pressed
            running = False # set running to False
        else: # if endkey has not been pressed
            wait(sec) # wait for sec seconds
    print("Stopped") # print stopped when autoclicker is stopped

# initialize window using tkinter
win = Tk()
win.title("Autoclicker")
win.geometry('600x200')
win.config(bg="#36454F") # set window background color

label = ttk.Label(win, text="Seconds in between clicks:", background='#36454F', foreground='#FFFFFF')
label.place(x=20,y=10,width=190,height=25)

# create dropdown menu from the seconds list
time_choice = StringVar(win)
time_choice.set(seconds[1]) # set default value to 0.1
time_dropdown = ttk.OptionMenu(win, time_choice, *seconds)
time_dropdown.place(x=230,y=10,width=70,height=25)

label_b = ttk.Label(win, text="Mouse button to click:", background='#36454F', foreground='#FFFFFF')
label_b.place(x=20,y=40,width=190,height=25)

# create dropdown menu from the mouse_buttons list
mb_choice = StringVar(win)
mb_choice.set(mouse_buttons[1]) # set default value to Left Click
mb_dropdown = ttk.OptionMenu(win, mb_choice, *mouse_buttons)
mb_dropdown.place(x=230,y=40,width=130,height=25)

# create start button which runs the autoclick function, passing user selections from dropdowns as paramaters
start_button = ttk.Button(win, text="Start", command=lambda: autoclick(time_choice.get(), mb_choice.get())) 
start_button.place(x=200,y=170,width=70,height=25)

# create quit button
quit_button = ttk.Button(win, text="Quit", command=win.destroy)
quit_button.place(x=300,y=170,width=70,height=25)

win.mainloop() # run the window
