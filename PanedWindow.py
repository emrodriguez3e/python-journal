import tkinter
from tkinter import *
from tkinter import ttk


class paneWindow(ttk.PanedWindow):
    def __init__(self, parent=None):
        ttk.PanedWindow.__init__(self, parent, orient='horizontal')
        self.leftPane = __import__('LeftPanel')
        self.rightPane = __import__('RightPanel')
        self.pack(expand=True, fill='both')

        self.list_pane = self.leftPane.leftPane()
        self.note_area = self.rightPane.rightPane()

        self.add(self.list_pane)
        self.add(self.note_area)

        self.note_area.text.insert(END,
                                   self.list_pane.tView.item(self.list_pane.tView.selection())['values'][0])

        self.list_pane.bind('<ButtonRelease>', self.cross)

    def cross(self, event=None):
        self.note_area = self.rightPane.text.get()

    def pane_control(self):
        pass

    def pane_forget(self, pane):
        self.forget(pane)


if __name__ == '__main__':
    paneWindow().mainloop()
