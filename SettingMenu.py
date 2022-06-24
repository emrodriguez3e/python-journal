from tkinter import *
from tkinter import ttk


class Settings(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        self.setting_text_frame = Frame(self)

        self.text = Text(self.setting_text_frame, width=50, height=7)
        self.font_size_scale = ttk.Scale(self.setting_text_frame)
        self.line_space_scale = ttk.Scale(self.setting_text_frame)

        self.pack(padx=15)
        self.setting_text_frame.pack()
        self.widgets()

    def widgets(self):
        self.text.pack(pady=5, expand=False)
        self.font_size_scale.pack()
        self.line_space_scale.pack()


if __name__ == '__main__':
    Settings().mainloop()
