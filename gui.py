import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

"""
printHelp is just a way to easily printout relevant data to a widget of tkinter
"""


def printhelp(i=0):
    try:
        print(i.configure().keys())
    except:
        print(str(i) + ' is not a valid input. Skipped.\n')


sampleString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, " \
               "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " \
               "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip" \
               " ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore " \
               "eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui " \
               "officia deserunt mollit anim id est laborum. "

root = Tk()
root.title("Python Journal")
root.geometry('500x400')

panedWindow = ttk.PanedWindow(root, orient=tkinter.HORIZONTAL)

# Create the table view and lean everything to the left
columns = ('name')
noteView = ttk.Treeview(root, columns=columns, show='headings')
noteView.pack(side=tkinter.LEFT, expand=True, fill='both')
noteView.heading('name', text='')



# Create ability to scroll through list of notes
notesScroll = ttk.Scrollbar(noteView, orient='vertical')
notesScroll.pack(side=tkinter.RIGHT)

# include table view into panedWindow
panedWindow.add(noteView)

# Create editable text and place onto the right
note = ScrolledText(root)
note.pack()
panedWindow.add(note)

panedWindow.pack(fill=tkinter.BOTH, expand=True)
root.mainloop()
