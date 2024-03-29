from tkinter import *
from tkinter import ttk
import os

"""
This file is for creating the gui from the top level
All modules make calls based on their relativity
"""


def check():
    # method to check if the directory exists.
    if os.path.exists('noteDirectory'):
        tkinter_app()
    else:
        os.mkdir('noteDirectory')
        tkinter_app()


def tkinter_app():

    root = Tk()  # create root window
    root.title('Python Journal')  # Label the window

    style = ttk.Style()
    style.configure("Custom.TFrame", background="black", foreground="white", font=("Helvetica", 12))


    # Create the area that the app will open initially
    w = 550
    h = 350
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/4) - (w/2)
    y = (hs/3) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set loading position
    root.minsize(width=450, height=300)  # set minimum window size

    pane_module = __import__('PanedWindow')  # import paneWindow
    pane_module.paneWindow(style="Custom.TFrame")  # Call PaneWindow

    root.mainloop()


if __name__ == '__main__':
    check()


