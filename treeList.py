from tkinter import *
from tkinter import ttk


class tree(ttk.Treeview):
    def __init__(self, parent=None, **options):
        ttk.Treeview.__init__(self, parent, **options)
        self.pack()

