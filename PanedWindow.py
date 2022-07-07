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

        self.list_pane.tView.bind('<ButtonRelease>', self.text_change)

    def text_change(self, event=None):
        # Grab text of item, delete current text then insert updated.
        item = self.list_pane.tView.item(self.list_pane.tView.selection()[0])['text']
        self.note_area.text.delete(0.0, END)
        self.note_area.text.insert(END, item)

    def update_note(self):
        # Grab text
        # TODO: Save note to correct item
        # TODO: Should get rid of side-effects
        new = self.note_area.text.get('1.0', 'end-1c')
        row_id = self.list_pane.tView.index(self.list_pane.tView.focus())
        print(row_id)

    def pane_control(self):
        pass

    def pane_forget(self, pane):
        self.forget(pane)


if __name__ == '__main__':
    paneWindow().mainloop()
