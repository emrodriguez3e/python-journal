import tkinter
from tkinter import *
from tkinter import ttk



def settingwidget(widget):
    # Need to see if the widget is present or not
    if widget.winfo_ismapped() == 1:
        widget.pack_forget()
    else:
        widget.pack(fill='x', side=tkinter.BOTTOM)


# Function meant to help get attributes of widgets
def printhelp(i=0):
    try:
        print(i.configure().keys())
    except:
        print(str(i) + ' is not a valid input. Skipped.\n')


# Create root
root = Tk()
root.title("Python Journal")  # Label the window
root.resizable(True, True)

# Create paned window to separate left pane against right pane
panedWindow = ttk.PanedWindow(root, orient=tkinter.HORIZONTAL, width=400, height=300)
noteFrame = ttk.Frame(root)  # This is the right pane

# Create the table view and lean everything to the left
columns = ('name')
noteView = ttk.Treeview(root, columns=columns, show='headings')
noteView.heading('name', text='')

settingPane = ttk.Frame(noteView)

# Create a button that can hide or un-hide settings
settingsBtn = ttk.Button(noteView, command=lambda: settingwidget(settingPane))
settingsBtn.place(relx=0.9, rely=0.95, anchor='se')

# Add settings to settingsPane
fontSize = ttk.Scale(settingPane, from_=0, to=100, orient='horizontal')
fontSize.grid(row=0, column=0)

fontSizeLabel = ttk.Label(settingPane, text='Sample')
fontSizeLabel.grid(row=0, column=1)

lineSpacing = ttk.Scale(settingPane, from_=0, to=100, orient='horizontal')
lineSpacing.grid(row=1, column=0)

lineSpacingLabel = ttk.Label(settingPane, text='Sample')
lineSpacingLabel.grid(row=1, column=1)


# Following two for loops populate treeView for testing purposes
contacts = []
for i in range(1, 100):
    contacts.append(str(i))

for contact in contacts:
    noteView.insert('', tkinter.END, values=contact)

# Create a thin loading bar; placed on the top
load = ttk.Progressbar(root, orient='horizontal', mode='determinate')
load.pack(fill='x')

# Create scroll bar for text editable frame; right side
noteScroll = ttk.Scrollbar(noteView, orient=tkinter.VERTICAL, command=noteView.yview)
noteScroll.pack(fill='y', side=tkinter.RIGHT)
noteView.pack(side=tkinter.LEFT, expand=True, fill='both')

# Create ability to scroll through list of notes; right side
text = Text(noteFrame, wrap='word')
scroll = ttk.Scrollbar(noteFrame, orient='vertical')
scroll.config(command=text.yview)
scroll.pack(side=tkinter.RIGHT, fill='y')
text.pack(fill='both', expand=True)  # need to pack text widget last for the scroll attachment


# Pack widgets into PanedWindow
panedWindow.add(noteView, weight=10)
panedWindow.add(noteFrame)

panedWindow.pack(fill=tkinter.BOTH, expand=True)  # Pack panedWindow

# Create an easy way to allow for resizing to occur, adds 3 dots in bottom right corner
grip = ttk.Sizegrip(root)
grip.pack(side=tkinter.RIGHT)

root.mainloop()
