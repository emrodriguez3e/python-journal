from tkinter import *
from tkinter import ttk


class Settings(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        self.setting_text_frame = Frame(self)

        self.text = Text(self, width=50, height=7)
        self.text.pack(pady=5, expand=False)

        self.font_label = Label(self.setting_text_frame, text="Sample")
        self.font_size_scale = ttk.Scale(self.setting_text_frame, orient=HORIZONTAL)
        self.line_label = Label(self.setting_text_frame, text="Sample")
        self.line_space_scale = ttk.Scale(self.setting_text_frame, orient=HORIZONTAL)

        self.pack(padx=15)
        self.setting_text_frame.pack(pady=15)
        self.widgets()

    def widgets(self):

        self.font_size_scale.grid(row=0, column=0)
        self.font_label.grid(row=0, column=1)
        self.line_space_scale.grid(row=1, column=0)
        self.line_label.grid(row=1, column=1)


if __name__ == '__main__':
    Settings().mainloop()
