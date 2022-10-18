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

frame = ttk.Frame(win, padding=0)
frame.grid()

ttk.Label(frame, text="Autoclicker").grid(column=0, row=0)

ttk.Label(frame, text="Seconds in between clicks").grid(column=2, row=0)
time_choice = StringVar(win)
time_choice.set(seconds[1])
time_dropdown = ttk.OptionMenu(win, time_choice, *seconds)
time_dropdown.grid(column=2, row=1)

mb_choice = StringVar(win)
mb_choice.set(mouse_buttons[1])
mb_dropdown = ttk.OptionMenu(win, mb_choice, *mouse_buttons)
mb_dropdown.grid(column=2, row=2)

ttk.Button(frame, text="Start", command=lambda: autoclick(time_choice.get(), mb_choice.get())).grid(column=1, row=3)
ttk.Button(frame, text="Quit", command=win.destroy).grid(column=1, row=4)

win.mainloop()
