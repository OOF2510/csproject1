from tkinter import *
from tkinter import ttk

def do_nothing():
    return

def add_range(list, amount):
    amount += 1
    for i in range(amount):
        if (i == 0):
            do_nothing()
        else:
            list.append(i)

seconds = []
add_range(seconds, 60)

def autoclick(ms, mousebutton):
    return print(f"{ms}, {mousebutton}")

win = Tk()
win.title("Autoclicker")
win.geometry('400x200')

frame = ttk.Frame(win, padding=0)
frame.grid()

ttk.Label(frame, text="Autoclicker").grid(column=0, row=0)

dropdown_default = StringVar(win)
dropdown_default.set(seconds[0])
dropdown = ttk.OptionMenu(win, dropdown_default, *seconds)
dropdown.grid(column=1, row=0)

ttk.Button(frame, text="Start", command=lambda: autoclick(2, 1)).grid(column=1, row=2)
ttk.Button(frame, text="Quit", command=win.destroy).grid(column=1, row=3)

win.mainloop()
