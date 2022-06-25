from tkinter import *



class rightPane(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent, width = 300)
        self.text = None
        self.right_click = None
        self.info_button = None
        self.pack(expand=True, fill='both')
        self.r_widgets()

    def r_widgets(self):

        self.info_button = Button(self, text="Text")
        self.info_button.pack(side=TOP)

        self.text = Text(self, wrap='word')
        self.text.pack(expand=True, fill='both')

        self.text.bind('<Button-2>', self.menu_pop_up)
        self.text.bind('<Button-3>', self.menu_pop_up)
        self.text.bind()

        self.right_click = Menu(self, tearoff=0)
        self.right_click.add_command(label='Cut')
        self.right_click.add_command(label='Copy')
        self.right_click.add_command(label='Paste')
        self.right_click.add_separator()
        self.right_click.add_command(label="Next")

    def menu_pop_up(self, event):
        try:
            self.right_click.tk_popup(event.x_root, event.y_root)
        finally:
            self.right_click.grab_release()


if __name__ == '__main__':
    rightPane().mainloop()
