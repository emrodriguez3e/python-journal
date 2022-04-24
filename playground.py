import tkinter
from tkinter import *
from tkinter import ttk
import os


root = Tk()
root.title("Playground")  # Label the window
root.resizable(True, True)
root.geometry('650x650')


def tree_fill():
    note_directory = os.path.join(os.getcwd(), 'noteDirectory')

    if not os.path.isdir(note_directory):
        os.mkdir(note_directory)
    else:
        # Currently, the files are overwritten everytime
        file = open('noteDirectory/untitled.txt', 'w')
        file.close()

        file = open('noteDirectory/untitled1.txt', 'w')


    list_amount = len(os.listdir(note_directory))

    for j in range(0, list_amount):
        treeView.insert('', tkinter.END, text=file.read(), values=("Note", ""))
    file.close()

def tree_item(event):
    pass

def get_body():
    pass


treeView = ttk.Treeview(columns='0', show='headings')
treeView.heading('0', text='')
treeView.bind('<<TreeviewSelect>>', tree_fill)

treeView.pack(expand=True, fill='both')

root.mainloop()

