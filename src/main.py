from tkinter import *
from tkinter import ttk
from pynput.mouse import Button, Controller
from pynput import keyboard
from time import sleep as wait

mouse_control = Controller()

def do_nothing():
    return

def add_range(list, amount):
    for i in range(amount):
        list.append(i)

seconds = []
add_range(seconds, 26)
mouse_buttons = ["Left Click", "Left Click", "Middle Click", "Right Click"]
buttonmap = {
    "Left Click": Button.left,
    "Middle Click": Button.middle,
    "Right Click": Button.right
}

endkey_pressed = False
def on_release(key):
    if key == keyboard.Key.esc:
        global endkey_pressed
        endkey_pressed = True

listener = keyboard.Listener(on_release=on_release)
listener.start()

running = False
def autoclick(sec, mb):
    mb = buttonmap[mb]
    sec = int(sec)
    global running
    global endkey_pressed
    running = True
    endkey_pressed = False
    print(f"Autoclicker started, press the 'esc' key twice to end")
    while running:
        mouse_control.press(mb)
        mouse_control.release(mb)
        if endkey_pressed == True:   
            running = False
        else:
            wait(sec)

win = Tk()
win.title("Autoclicker")
win.geometry('600x200')

label = ttk.Label(win, text="Seconds in between clicks:")
label.place(x=20,y=10,width=190,height=25)

time_choice = StringVar(win)
time_choice.set(seconds[1])
time_dropdown = ttk.OptionMenu(win, time_choice, *seconds)
time_dropdown.place(x=230,y=10,width=70,height=25)

label = ttk.Label(win, text="Mouse button to click:")
label.place(x=20,y=40,width=190,height=25)

mb_choice = StringVar(win)
mb_choice.set(mouse_buttons[1])
mb_dropdown = ttk.OptionMenu(win, mb_choice, *mouse_buttons)
mb_dropdown.place(x=230,y=40,width=130,height=25)

start_button = ttk.Button(win, text="Start", command=lambda: autoclick(time_choice.get(), mb_choice.get()))
start_button.place(x=200,y=170,width=70,height=25)

quit_button = ttk.Button(win, text="Quit", command=win.destroy)
quit_button.place(x=300,y=170,width=70,height=25)

win.mainloop()
