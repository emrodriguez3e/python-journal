from tkinter import *
from tkinter import ttk


class rightPane(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        self.main_upper = Frame(self)
        self.main_lower = Frame(self)

        self.info_panel = Frame(self.main_lower, width=100)
        self.setting_upper = Frame(self.info_panel)
        self.setting_lower = Frame(self.info_panel)

        self.text = Text(self.main_lower, bg='#333333', wrap='word', borderwidth=0, bd=0, highlightthickness=0)

        self.list_button = ttk.Button(self.main_upper, text='<')

        self.info_button = ttk.Button(self.main_upper, text='i', command=self.info_pack)

        # Build everything for the top section of the info panel
        self.char_count = Label(self.setting_upper, text='0 ')
        self.char_label = Label(self.setting_upper, text='Characters ')

        self.word_label = Label(self.setting_upper, text='Words ')
        self.word_count = Label(self.setting_upper, text='0')

        self.read_label = Label(self.setting_upper, text='Read Time ')
        self.read_count = Label(self.setting_upper, text='0M ')

        self.para_label = Label(self.setting_upper, text='Paragraphs ')
        self.para_count = Label(self.setting_upper, text='0 ')


        # Build for the bottom section of the info panel
        self.docx_Label = Label(self.setting_lower, text='WORD')
        self.docx_Label.grid(row=0, column=1)
        self.txt_label = Label(self.setting_lower, text='TXT')
        self.txt_label.grid(row=0, column=2)
        self.pdf_label = Label(self.setting_lower, text='PDF')
        self.pdf_label.grid(row=0, column=3)

        self.right_click = Menu(self, tearoff=0)

        self.pack(expand=True, fill='both', padx=5)
        self.setting_widgets()
        self.r_widgets()

        self.text.bind('<KeyRelease>', self.info_update)

    def r_widgets(self):

        self.main_upper.pack(fill='x', padx=3)
        self.main_lower.pack(fill='both', expand=True)

        self.setting_upper.pack()
        self.setting_lower.pack()

        self.info_button.pack(side=RIGHT)

        self.text.pack(side=LEFT, fill='both', expand=True, padx=50)

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
            self.info_panel.pack(side=RIGHT, before=self.text)

    def menu_pop_up(self, event):
        try:
            self.right_click.tk_popup(event.x_root, event.y_root)
        finally:
            self.right_click.grab_release()

    def info_update(self, event=None):
        body = self.text.get('1.0', 'end-1c')
        self.char_count.config(text=len(body))
        self.word_count.config(text=len(body.split()))
        self.para_count.config(text=len(body.split('\n\n')))

    def hidden_panel(self, event=None):
        self.list_button.pack(side=LEFT)


if __name__ == '__main__':
    rightPane().mainloop()
