import tkinter
from tkinter import *
from tkinter import ttk


class paneWindow(ttk.PanedWindow):
    def __init__(self, parent=None):
        ttk.PanedWindow.__init__(self, parent, orient='horizontal')
        self.l_pane = __import__('LeftPanel')
        self.r_pane = __import__('RightPanel')
        self.pack(expand=True, fill='both')
        self.make_widgets()

        self.bind('<Control-n>', self.l_pane.leftPane.create_new_note_bind)

    def make_widgets(self):

        self.add(self.l_pane.leftPane())
        self.add(self.r_pane.rightPane())


if __name__ == '__main__':
    paneWindow().mainloop()
