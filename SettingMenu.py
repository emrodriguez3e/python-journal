from tkinter import *
from tkinter import ttk


class Settings(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        self.setting_buttons = Frame(self)
        self.setting_buttons.pack(fill='x', expand=False)

        self.typography_button = ttk.Button(self.setting_buttons, text='Typography')
        self.typography_button.grid(row=0, column=0, padx=3, pady=3)
        self.themes_button = ttk.Button(self.setting_buttons, text='Themes')
        self.themes_button.grid(row=0, column=1, padx=3, pady=3)

        self.setting_text_frame = Frame(self)

        self.text = Text(self, width=30, height=15, wrap='word')
        self.text.pack()

        self.font_label = Label(self.setting_text_frame, text="Sample")
        self.font_size_scale = ttk.Scale(self.setting_text_frame, orient=HORIZONTAL, from_=0, to=5)
        self.line_label = Label(self.setting_text_frame, text="Sample")
        self.line_space_scale = ttk.Scale(self.setting_text_frame, orient=HORIZONTAL)

        self.pack(padx=5)
        self.setting_text_frame.pack(pady=5)
        self.widgets()

    def widgets(self):
        self.font_size_scale.grid(row=0, column=0)
        self.font_label.grid(row=0, column=1)
        self.line_space_scale.grid(row=1, column=0)
        self.line_label.grid(row=1, column=1)


if __name__ == '__main__':
    Settings().mainloop()
