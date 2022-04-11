from tkinter import *
from tkinter import ttk

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

frame = ttk.Frame(root, padding=10)
frame.grid()

introLabel = ttk.Label(frame, text="Hello!")
introLabel.grid(column=0, row=0)

loremString = ttk.Label(frame, text=sampleString)
loremString.grid(column=1, row=0)

# separate commands for a widget below allows the ability to print its attributes
quitButton = ttk.Button(frame, text='Quit', command=root.destroy)
quitButton.grid(column=0, row=2)

root.mainloop()
