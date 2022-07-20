from tkinter import *
from tkinter import ttk


class Settings(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)


        # Build frames necessary for this widget
        self.setting_buttons = Frame(self)
        self.setting_buttons.pack(fill='x', expand=False)
        
        self.setting_text_frame = Frame(self) # Houses all text characteristics
        self.themes_frame = Frame(self) # Houses color schemes

        #Create buttons to switch between views. 
        self.typography_button = ttk.Button(self.setting_buttons,
                                            text='Typography',
                                            command=self.typography_widgets)
        self.typography_button.grid(row=0, column=0, padx=3, pady=3)
        
        self.themes_button = ttk.Button(self.setting_buttons,
                                        text='Themes',
                                        command=self.themes_widget)
        self.themes_button.grid(row=0, column=1, padx=3, pady=3)

        
        # Text area that should not be editable at all.
        # Meant to show the preview of the text before applying it to all notes
        self.text = Text(self, width=30, height=15, wrap='word')
        self.text.insert(END, 'This is a sample text')
        self.text['state'] = 'disabled' #Text should not be editable
        self.text.pack()

        # Label & Scale for typography frame
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

    def typography_widgets(self):
        self.setting_text_frame.forget()
        self.themes_frame.pack()
        self.typography_button['state'] = 'disabled'
        self.themes_button['state'] = 'active'

    def themes_widget(self):
        self.themes_frame.forget()
        self.setting_text_frame.pack()
        self.typography_button['state'] = 'active'
        self.themes_button['state'] = 'disabled'


if __name__ == '__main__':
    Settings().mainloop()
