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
               " ex ea commodo consequat. Duis aute irure dolor in reprehen derit in voluptate velit esse cillum dolore " \
               "eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui " \
               "officia deserunt mollit anim id est laborum. "



root = Tk()
root.title("Python Journal")
root.geometry('500x400')

panedWindow = ttk.PanedWindow(root, orient=tkinter.HORIZONTAL)
noteFrame = ttk.Frame(root)

# Create the table view and lean everything to the left
columns = ('name')
noteView = ttk.Treeview(root, columns=columns, show='headings')
noteView.heading('name', text='')


# ollowing code populates the tree view
contacts = []
for i in range(1,100):
    contacts.append(str(i))

for contact in contacts:
    noteView.insert('', tkinter.END, values=contact)

noteScroll = ttk.Scrollbar(noteView, orient=tkinter.VERTICAL, command=noteView.yview)
noteScroll.pack(fill='y', side=tkinter.RIGHT)
noteView.pack(side=tkinter.LEFT, expand=True, fill='both')

# Create ability to scroll through list of notes
text = Text(noteFrame, wrap='word')
scroll = ttk.Scrollbar(noteFrame, orient='vertical')
scroll.config(command=text.yview)
scroll.pack(side=tkinter.RIGHT, fill='y')
text.pack(fill='both', expand=True) #need to pack text widget last for the scroll attachment

# Create editable text and place onto the right
note = ScrolledText(root)


# Pack widgets into PanedWindow
panedWindow.add(noteView)
panedWindow.add(noteFrame)

panedWindow.pack(fill=tkinter.BOTH, expand=True)
root.mainloop()
