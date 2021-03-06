import tkinter
from tkinter import *
from tkinter import ttk
import os
import datetime
import time

"""
All file manipulations should be done here
Reading/Writing/Updating should be held in this area
"""


def note_name():
    # Function that creates the name of the file
    local = time.localtime()

    file_name = str(local.tm_year) + "-" + \
                str(local.tm_mon) + "-" + \
                str(local.tm_mday) + "-" + \
                str(local.tm_hour) + "-" + \
                str(local.tm_min) + "-" + \
                str(local.tm_sec) + "-" + \
                str(int(round((time.time() % 1), 2) * 100)) + '.txt'

    return str(file_name)


class Tree(ttk.Treeview):
    # Subclass of ttk.TreeView
    def __init__(self, parent=None, *args):
        # Creates subclass

        self.style = ttk.Style()
        self.style.configure('Treeview', background='#121212', fieldbackground='#121212')


        ttk.Treeview.__init__(self,
                              parent,
                              columns='noteHeader',
                              show='tree',
                              style='Treeview'
                              )

        self.column('#0', minwidth=25, width=25, stretch=False, anchor='center')
        self.column('#1', minwidth=75, width=200, stretch=True)

        self.file = None
        self.pin_image = PhotoImage(file='media/pin.png')
        self.pin_sample = self.pin_image.subsample(60, 60)

        self.bind('<Button-2>', self.menu_popup)
        self.bind('<Button-3>', self.menu_popup)
        self.bind('<Command-BackSpace>')
        self.bind('<Control-d>', self.d)

        self.right_click = Menu(self, tearoff=0)
        self.right_click.add_command(label='Duplicate', command=self.duplicate_note)
        self.right_click.add_command(label='Delete', command=self.delete_item)
        self.right_click.add_separator()
        # self.right_click.add_command(label='Merge')
        # self.right_click.add_command(label='Open In New Window')
        self.right_click.add_command(label='Pin', command=self.pin)

        self.pack(expand=True, fill='both')
        self.tree_load()



    def menu_popup(self, event):
        # Right click menu that is based on coordinates of the mouse that is within TreeView.py
        self.selection_set(self.identify_row(event.y))

        try:
            self.right_click.tk_popup(event.x_root, event.y_root)
        finally:
            self.right_click.grab_release()

    def tree_load(self):
        # When the tree is loading, load the list in a sorted fashion with the newest note being on top

        if len(os.listdir('noteDirectory')) == 0:
            return

        load_list = []

        if not os.path.isdir('noteDirectory'):  # checks if the dir exists
            os.mkdir('noteDirectory')

        if len(os.listdir('noteDirectory')) == 0:
            pass
        else:
            for i in os.listdir('noteDirectory'):
                if not i == '.DS_Store':
                    a = os.stat(os.path.join('noteDirectory', i))
                    load_list.append([time.ctime(a.st_ctime), i])

        for i in sorted(load_list, reverse=True):
            file = open('noteDirectory/' + str(i[1]), 'r')
            note = file.read()
            self.insert('', 'end', text="", values=(note[:25], note, i[1]))
            file.close()

        self.selection_set(self.get_children()[0])

    def new_note(self):
        # Will create a new note and set the tree selection to be the newest note which is at the top of the list
        file_name = note_name()
        file = open('noteDirectory/' + file_name, 'w')
        body = 'New Note ' + file_name
        file.write(body)
        file.close()
        self.insert('', index=0, values=(body[:25], body, file_name))
        self.selection_set(self.get_children()[0])

    def duplicate_note(self, event=None):
        # Finds the correct file to acquire the name of the note and the body of the note.
        # Will create a new note with 'copy' at the end and will write the same body of text to said note

        children_names = [] * len(self.get_children())
        for i in self.get_children():
            children_names.append(self.item(i)['values'][2])

        file = open('noteDirectory/' + self.item(self.selection())['values'][2], 'r')
        copy = file.read()
        file.close()

        # Duplicate that note
        file_name = self.item(self.selection())['values'][2].replace('.txt', ' copy.text')

        while file_name in children_names:
            file_name = file_name.replace('copy', 'copy copy', 1)

        row_id = self.index(self.selection())
        file = open('noteDirectory/' + file_name, 'w')
        file.write(copy)
        file.close()

        # insert note after duplicated note
        self.insert('', index=row_id, values=(copy[:25], copy, file_name))

    def delete_item(self, event=None):
        # This should find the item, delete it as well as remove it from self
        if self.get_children() == 0:  # If there is no item to delete
            return
        if len(self.selection()) == 0:  # If there is no selection
            return

        if self.index(self.selection()) == 0:
            note_id = self.index(self.selection()) + 1
        elif self.index(self.selection()) == len(self.get_children())-1:
            note_id = self.index(self.selection()) - 1

        os.remove('noteDirectory/' + self.item(self.selection())['values'][2])
        self.delete(self.selection())
        if len(self.get_children()) == 0:
            return
        self.selection_set(self.get_children()[note_id])
        print(self.get_children())

    def get_body(self, event=None):
        # Should return the selected cell and return the note body
        if len(self.get_children()) == 0:
            return
        return self.item(self.selection())['values'][1]

    def pin(self):
        # If there is no image attached, add image.
        # If there is an image attached, removed image
        if self.item(self.selection())['image'] == "":
            self.item(self.selection(), image=self.pin_sample)
        elif self.item(self.selection())['image'] != "":
            self.item(self.selection(), image="")

    def d(self, event=None):
        # hitting control d will run this code block.
        print(len(self.selection()) == 0)


if __name__ == '__main__':
    Tree().mainloop()
