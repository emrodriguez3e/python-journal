import tkinter
from tkinter import *
from tkinter import ttk
import os
import time


class leftPane(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent, width=300)
        self.Tree = __import__('TreeView')

        self.cog_sample = None
        self.plus_sample = None

        self.upper_frame = Frame(self)
        self.lower_frame = Frame(self)

        self.setting_button = ttk.Button(self.upper_frame, compound=CENTER)
        self.new_note = ttk.Button(self)

        # self.t_view = ttk.Treeview
        self.right_click = None
        self.body = None
        self.pack(fill='both', expand=True)
        self.tView = self.Tree.Tree(parent=self.lower_frame)

        self.tView.bind('<ButtonRelease>', self.get_body)

        self.l_widgets()

    def l_widgets(self):

        self.upper_frame.pack(fill='x')
        self.lower_frame.pack(fill='both', expand=True)  # to keep Tree big

        b_i_s = 7  # button_image_size
        cog = PhotoImage(file=r"media/cog.png")
        self.cog_sample = cog.subsample(b_i_s, b_i_s)
        plus = PhotoImage(file=r"media/plus.png")
        self.plus_sample = plus.subsample(b_i_s + 9, b_i_s + 9)

        self.setting_button.config(image=self.cog_sample)
        self.setting_button.pack(side=tkinter.LEFT, padx=5)

        self.new_note.config(image=self.plus_sample, command=self.tView.new_note)
        self.new_note.place(relx=0.9, rely=0.95, anchor='se')

    def get_body(self, event=None):
        body = self.tView.get_body()
        return body


if __name__ == '__main__':
    leftPane().mainloop()
