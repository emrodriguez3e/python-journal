import tkinter
from tkinter import *
from tkinter import ttk
import os


class leftPane(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent, width=300)
        self.cog_sample = None
        self.plus_sample = None
        self.upper_frame = Frame(self)
        self.lower_frame = Frame(self)

        self.t_view = ttk.Treeview
        self.right_click = None
        self.pack(fill='both', expand=True)
        self.l_widgets()

    def l_widgets(self):
        # self.upper_frame = Frame(self)
        self.upper_frame.pack()
        # self.lower_frame = Frame(self)
        self.lower_frame.pack(fill='both', expand=True)  # to keep tree big

        b_i_s = 7  # button_image_size
        cog = PhotoImage(file=r"media/cog.png")
        self.cog_sample = cog.subsample(b_i_s, b_i_s)
        plus = PhotoImage(file=r"media/plus.png")
        self.plus_sample = plus.subsample(b_i_s + 9, b_i_s + 9)

        ttk.Button(self.upper_frame, image=self.cog_sample, compound=CENTER).pack(side=tkinter.LEFT)
        Entry(self.upper_frame).pack(side=tkinter.RIGHT)

        ttk.Button(self, image=self.plus_sample, compound=CENTER).place(relx=0.9, rely=0.95, anchor='se')

        self.t_view = ttk.Treeview(self.lower_frame, columns='0', show='headings')
        self.t_view.pack(side=tkinter.BOTTOM, fill='both', expand=True)

        self.t_view.bind('<Button-2>', self.menu_pop_up)
        self.t_view.bind('<Button-3>', self.menu_pop_up)

        self.right_click = Menu(self, tearoff=0)
        self.right_click.add_command(label='Duplicate')
        self.right_click.add_command(label='Delete')
        self.right_click.add_command(label='Rename')
        self.right_click.add_separator()
        self.right_click.add_command(label='Merge')
        self.right_click.add_command(label='Open In New Window')
        self.right_click.add_command(label='Info')

    def menu_pop_up(self, event):
        try:
            self.right_click.tk_popup(event.x_root, event.y_root)
        finally:
            self.right_click.grab_release()


if __name__ == '__main__':
    leftPane().mainloop()
