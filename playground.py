import time
import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import os
from tkinter import font as tkfont

def settings_widget():
    setting_frame = Toplevel(root)

    l = Label(setting_frame, text='Test')


root = Tk()
# Initial width and height dimensions
w = 600/2
h = 500/2

# Get screen info
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# Calculate x and y for Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

frame = Frame(root)

print()

Btn = Button(frame, text='Test', command=settings_widget)

Btn.pack()
frame.pack()

root.mainloop()