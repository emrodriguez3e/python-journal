from tkinter import *
from tkinter import ttk

"""
Only pinned notes should be modified here

"""


class pinView(ttk.Treeview):
    def __init__(self, parent=None):
        ttk.Treeview.__init__(self, parent, columns=0, show='headings')

        self.file = None

        self.right_click = Menu(self, tearoff=0)

        self.pack()
        self.load()

    def menu_pop(self, event=None):
        try:
            self.right_click.tk_popup(event.x_root, event.y_root)
        finally:
            self.right_click.grab_release()

    def load(self):
        pass
