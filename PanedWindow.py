import tkinter
from tkinter import *
from tkinter import ttk

"""
This class subclasses the ttk.PanedWindow widget
Calls both LeftPanel.py and RightPanel.py
Cross functions such as list view to note view and vice versa is done here
"""


class paneWindow(ttk.PanedWindow):
    # Subclass ttk.PanedWindow
    def __init__(self, parent=None):
        # Init
        ttk.PanedWindow.__init__(self, parent, orient='horizontal')

        # import proper py files
        self.leftPane = __import__('LeftPanel')
        self.rightPane = __import__('RightPanel')
        self.pack(expand=True, fill='both')

        # instantiate objects of imported files
        self.list_pane = self.leftPane.leftPane()
        self.note_area = self.rightPane.rightPane()

        # Add objects to self subclass
        self.add(self.list_pane)
        self.add(self.note_area)

        # Automatically load the top note into text area
        self.note_area.text.insert(END,
                                   self.list_pane.tView.item(self.list_pane.tView.selection())['values'][0])

        # Bindings
        self.list_pane.tView.bind('<ButtonRelease>', self.text_change)

    def text_change(self, event=None):
        # Grab text of item, delete current text then insert updated.
        # TODO: Should change when a new note is created
        item = self.list_pane.tView.item(self.list_pane.tView.selection()[0])['text']
        self.note_area.text.delete(0.0, END)
        self.note_area.text.insert(END, item)

    def update_note(self):
        # Grab text
        # TODO: Save note to corresponding file
        # TODO: Should get rid of side-effects
        new = self.note_area.text.get('1.0', 'end-1c')
        row_id = self.list_pane.tView.index(self.list_pane.tView.focus())
        print(row_id)

    def pane_control(self):
        pass

    def pane_forget(self, pane):
        # If the window is less than a specific size, then the note list will be hidden
        # If panedwindow sash is to the left, then this should be called as well
        # TODO: If the size of window is less than a certain amount, then forget the list pane
        self.forget(pane)

    def d(self, event=None):
        # Debug function; mainly overwrite code here as gui.py has bind to this function
        print('here')
        print(self.winfo_width())


if __name__ == '__main__':
    paneWindow().mainloop()
