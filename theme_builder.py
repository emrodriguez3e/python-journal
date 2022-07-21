from tkinter import *
from tkinter import ttk

"""
This file is to help experiment with various themes. 
Just note, that there is naming conventions for the various stylings

"""


class Theme(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        self.styling = ttk.Style()
        # self.styling.configure("W.TButton",  activebackground='black')

        self.btn = Button(self, text='Sample button', bg='yellow')
        self.btn.pack(padx=10)

        self.pack()


if __name__ == '__main__':
    Theme().mainloop()
