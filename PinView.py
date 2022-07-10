from tkinter import *
from tkinter import ttk

"""
Only pinned notes should be modified here

"""


class PinView(ttk.Treeview):
    def __init__(self, parent=None):
        ttk.Treeview.__init__(self, parent,
                              columns=('noteHeader'),
                              show='tree',
                              height=14
                              )

        self.column('#0', minwidth=30, width=30, stretch=False)
        self.column('#1', minwidth=70, width=100, stretch=True)

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

if __name__ == '__main__':
    pinView().mainloop()
