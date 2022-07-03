import tkinter
from tkinter import *
from tkinter import ttk
import os
import datetime
import time


class Tree(ttk.Treeview):
    def __init__(self, parent=None):
        ttk.Treeview.__init__(self,
                              parent,
                              columns='0',
                              show='headings'
                              )

        self.bind('<Button-2>', self.menu_popup)
        self.bind('<Button-3>', self.menu_popup)
        self.bind('<Command-BackSpace>')
        self.bind('<ButtonRelease>', self.get_body)

        self.right_click = Menu(self, tearoff=0)
        self.right_click.add_command(label='Duplicate')
        self.right_click.add_command(label='Delete')
        self.right_click.add_command(label='Rename')
        self.right_click.add_separator()
        self.right_click.add_command(label='Merge')
        self.right_click.add_command(label='Open In New Window')
        self.right_click.add_command(label='Pin')

        self.pack(expand=True, fill='both')
        self.tree_load()


    def menu_popup(self, event):
        try:
            self.right_click.tk_popup(event.x_root, event.y_root)
        finally:
            self.right_click.grab_release()

    def tree_load(self):
        if not os.path.isdir('noteDirectory'):
            os.mkdir('noteDirectory')

        if len(os.listdir('noteDirectory')) == 0:
            pass
        else:
            for i in sorted(os.listdir('noteDirectory'), reverse=False):
                if i != '.DS_Store':
                    file = open('noteDirectory/' + str(i), 'r')
                    note_title = file.read(15)
                    self.insert('', 0, text=file.read(), values=(note_title, ''))
                    file.close()
            self.selection_set(self.get_children()[0])


    def note_name(self):
        local = time.localtime()

        file_name = str(local.tm_year) + "-" + \
                    str(local.tm_mon) + "-" + \
                    str(local.tm_mday) + "-" + \
                    str(local.tm_hour) + "-" + \
                    str(local.tm_min) + "-" + \
                    str(local.tm_sec) + "-" + \
                    str(int(round((time.time() % 1), 2)*100)) + '.txt'

        return str(file_name)

    def new_note(self):
        file_name = self.note_name()
        file = open('noteDirectory/' + file_name, 'w')
        body = 'New Note'
        file.write(body)
        file.close()
        self.insert('', index=0, text=body, values=([body]))

    def duplicate_note(self):
        file = open('noteDirectory/' + self.item(self.selection())['values'][0], 'r')
        copy = file.read()
        file.close()

        print(copy)

        # Duplicate that note
        file_name = self.item(self.selection())['values'][0].replace('.txt', '') + ' copy.txt'
        row_id = self.index(self.selection())
        file = open('noteDirectory/' + file_name, 'w')
        body = copy
        file.write(body)
        file.close()

        # insert note after duplicated note
        self.insert('', row_id, text=body, values=(file_name, ''))

    def delete_item(self, event=None):
        os.remove('noteDirectory/' + self.item(self.selection())['values'])
        self.delete(self.selection())

    def get_body(self):
        return self.item(self.selection())['values'][0]


if __name__ == '__main__':
    Tree().mainloop()
