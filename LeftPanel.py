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
        self.tree_load()

    def l_widgets(self):

        self.upper_frame.pack()
        self.lower_frame.pack(fill='both', expand=True)  # to keep tree big

        b_i_s = 7  # button_image_size
        cog = PhotoImage(file=r"media/cog.png")
        self.cog_sample = cog.subsample(b_i_s, b_i_s)
        plus = PhotoImage(file=r"media/plus.png")
        self.plus_sample = plus.subsample(b_i_s + 9, b_i_s + 9)

        ttk.Button(self.upper_frame, image=self.cog_sample, compound=CENTER).pack(side=tkinter.LEFT)
        Entry(self.upper_frame).pack(side=tkinter.RIGHT)

        ttk.Button(self,
                   image=self.plus_sample,
                   compound=CENTER,
                   command=self.create_new_note).place(relx=0.9,
                                                       rely=0.95,
                                                       anchor='se')

        self.t_view = ttk.Treeview(self.lower_frame, columns='0', show='headings')
        self.t_view.pack(side=tkinter.BOTTOM, fill='both', expand=True)

        self.t_view.bind('<Button-2>', self.menu_pop_up)
        self.t_view.bind('<Button-3>', self.menu_pop_up)
        self.t_view.bind('<Command-BackSpace>', self.t_view_delete_event)

        self.right_click = Menu(self, tearoff=0)
        self.right_click.add_command(label='Duplicate', command=self.t_view_duplicate)
        self.right_click.add_command(label='Delete', command=self.t_view_delete)
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

    def tree_load(self):
        if not os.path.isdir('noteDirectory'):
            os.mkdir('noteDirectory')
        for i in os.listdir('noteDirectory'):
            if not i == '.DS_Store':
                file = open('noteDirectory/' + i, 'r')
                self.t_view.insert('', tkinter.END, text=file.read(), values=(i, ""))
                file.close()

    def create_new_note(self):
        if len(self.t_view.get_children()) == 0:
            new_note = 'untitled1.txt'
        else:
            for i in self.t_view.get_children():
                if 'untitled' in self.t_view.item(i)['values'][0] and not 'copy' in self.t_view.item(i)['values'][0]:
                    note_name = self.t_view.item(i)['values'][0].replace('untitled', '')
                    note_name = note_name.replace('.txt', '')

            newest_note = 'untitled' + str(int(note_name) + 1) + '.txt'

        file = open('noteDirectory/' + newest_note, 'w')
        body = 'This is a new note'
        file.write(body)
        file.close()
        self.t_view.insert('', tkinter.END, text=body, values=(newest_note, ""))

    def create_new_note_bind(self, event):
        self.create_new_note()

    def t_view_duplicate(self):
        file = open('noteDirectory/' + self.t_view.item(self.t_view.selection())['values'][0], 'r')
        copy = file.read()
        file.close()

        print(copy)

        # Duplicate that note
        file_name = self.t_view.item(self.t_view.selection())['values'][0].replace('.txt', '') + ' copy.txt'
        row_id = self.t_view.index(self.t_view.selection())
        file = open('noteDirectory/' + file_name, 'w')
        body = copy
        file.write(body)
        file.close()

        # insert note after duplicated note
        self.t_view.insert('', row_id, text=body, values=(file_name, ''))

    def t_view_delete(self):
        os.remove('noteDirectory/' + self.t_view.item(self.t_view.selection())['values'][0])
        self.t_view.delete(self.t_view.selection())

    def t_view_delete_event(self, event):
        for i in self.t_view.selection():
            os.remove('noteDirectory/'+self.t_view.item(i)['values'][0])
            self.t_view.delete(i)


if __name__ == '__main__':
    leftPane().mainloop()
