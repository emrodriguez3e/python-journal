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

        # import proper relevant files
        self.leftPane = __import__('LeftPanel')
        self.rightPane = __import__('RightPanel')
        self.pack(expand=True, fill='both')


        # instantiate objects of imported files
        self.list_pane = self.leftPane.leftPane()
        self.note_area = self.rightPane.rightPane()
        self.note_area.list_button.config(command=self.list_pane_add)

        # Add objects to self subclass
        self.add(self.list_pane)
        self.add(self.note_area)

        print(self.panes())

        # Automatically load the top note into text area
        self.note_area.text.insert(END,
                                   self.list_pane.tView.item(self.list_pane.tView.selection())['values'][0])

        # Bindings
        self.bind('<ButtonRelease>', self.sash_adjustment)
        self.bind('<Control-d>', self.list_pane_add)

        self.list_pane.tView.bind('<ButtonRelease>', self.note_change)
        self.list_pane.tView.bind('<Control-d>', self.debuger)

        self.note_area.info_update()
        self.note_area.text.bind('<KeyRelease>', self.update_note)

    def note_change(self, event=None):
        # Changes the body of the note based on the next selection
        # Grab text of item, delete current text then insert updated.
        # TODO: Should change when a new note is created
        item = self.list_pane.tView.item(self.list_pane.tView.selection())['text']
        self.note_area.text.delete(0.0, END)
        self.note_area.text.insert(END, item)
        self.note_area.info_update()

    def update_note(self, event=None):
        # Grab text
        # TODO: Save note to corresponding file
        # TODO: Should get rid of side-effects
        # Grab Text
        new = self.note_area.text.get('1.0', 'end-1c')
        self.note_area.info_update()

        # get file name
        file_name = self.list_pane.tView.item(self.list_pane.tView.selection())['values'][1]
        file = open('noteDirectory/'+file_name, 'w')
        file.write(new)  # overwrite note body

        # update item
        self.list_pane.tView.item(item=self.list_pane.tView.selection(),
                                  text=new)  # this updates note body
        self.list_pane.tView.item(item=self.list_pane.tView.selection(),
                                  values=(new[:10],
                                          self.list_pane.tView.item(self.list_pane.tView.selection())['values'][1]))
        file.close()  # close file

    def pane_control(self):
        pass

    def sash_adjustment(self, event=None):
        if not len(self.panes()) < 2:  # checks if two panes exist.
            if self.sashpos(0) < 100:
                self.forget('.!leftpane')  # once this is called, an error occurs
                self.note_area.hidden_panel()

    def list_pane_add(self, event=None):
        self.insert(0, self.list_pane)
        self.note_area.list_button.forget()


    def debuger(self, event=None):
        print(self.list_pane.tView.item(self.list_pane.tView.selection()))


if __name__ == '__main__':
    paneWindow().mainloop()
