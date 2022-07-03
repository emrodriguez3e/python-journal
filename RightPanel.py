from tkinter import *
from tkinter import ttk


class rightPane(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.upperFrame = Frame(self)
        self.lowerFrame = Frame(self)

        self.text = Text(self.lowerFrame, wrap='word')

        self.info_panel = Frame(self.lowerFrame, width=100)
        self.info_button = ttk.Button(self.upperFrame, text='i', command=self.info_pack)

        self.char_label = Label(self.info_panel, text='Characters ')
        self.char_count = Label(self.info_panel, text='0 ')

        self.word_label = Label(self.info_panel, text='Words ')
        self.word_count = Label(self.info_panel, text='0')

        self.read_label = Label(self.info_panel, text='Read Time ')
        self.read_count = Label(self.info_panel, text='0M ')

        self.para_label = Label(self.info_panel, text='Paragraphs ')
        self.para_count = Label(self.info_panel, text='0 ')

        self.right_click = Menu(self, tearoff=0)

        self.pack(expand=True, fill='both', padx=5)
        self.setting_widgets()
        self.r_widgets()

    def r_widgets(self):

        self.upperFrame.pack(fill='x', padx=3)
        self.lowerFrame.pack(fill='both', expand=True)
        self.info_button.pack(side=RIGHT)

        self.text.pack(side=LEFT, fill='both', expand=True)

        self.text.bind('<Button-2>', self.menu_pop_up)
        self.text.bind('<Button-3>', self.menu_pop_up)

        self.right_click.add_command(label='Cut')
        self.right_click.add_command(label='Copy')
        self.right_click.add_command(label='Paste')
        self.right_click.add_separator()
        self.right_click.add_command(label="Next")

    def setting_widgets(self):

        self.word_label.grid(row=0, column=0)
        self.word_count.grid(row=1, column=0)

        self.char_label.grid(row=0, column=1)
        self.char_count.grid(row=1, column=1)

        self.read_label.grid(row=2, column=0)
        self.read_count.grid(row=3, column=0)

        self.para_label.grid(row=2, column=1)
        self.para_count.grid(row=3, column=1)

    def info_pack(self, event=None):

        if self.info_panel.winfo_ismapped() == 1:
            self.info_panel.forget()
        else:
            self.info_panel.pack(side=RIGHT)

    def menu_pop_up(self, event):
        try:
            self.right_click.tk_popup(event.x_root, event.y_root)
        finally:
            self.right_click.grab_release()


if __name__ == '__main__':
    rightPane().mainloop()
