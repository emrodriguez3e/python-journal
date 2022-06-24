import tkinter
from tkinter import *
from tkinter import ttk


class paneWindow(ttk.PanedWindow):
    def __init__(self, parent=None):
        ttk.PanedWindow.__init__(self, parent, orient='horizontal')
        self.pack(expand=True, fill='both')
        self.make_widgets()

    def make_widgets(self):
        l_pane = __import__('LeftPanel')
        r_pane = __import__('RightPanel')

        self.add(l_pane.leftPane())
        self.add(r_pane.rightPane())


if __name__ == '__main__':
    paneWindow().mainloop()
