import tkinter
from tkinter import *
from tkinter import ttk

# Create root
root = Tk()
root.title("Python Journal")  # Label the window
root.resizable(True, True)


def settingwidget(widget):
    # Need to see if the widget is present or not
    # If 1, then it is visible
    if widget.winfo_ismapped() == 1:
        widget.pack_forget()
    else:
        widget.pack()


def getfontsize():
    return '{: .2f}'.format(fontSizeValue.get())

def getlinespace():
    return '{: .2f}'.format(lineSpacingValue.get())


def linespacingchanged(event):
    lineSpacingLabel.configure(text=getlinespace())

def fontsizechanged(event):
    fontSizeLabel.configure(text=getfontsize())


# Function meant to help get attributes of widgets
def printhelp(i=0):
    try:
        print(i.configure().keys())
    except:
        print(str(i) + ' is not a valid input. Skipped.\n')


# Load Media
cogSize = 7
cog = PhotoImage(file=r"media/cog.png")
cogSample = cog.subsample(cogSize, cogSize)

# Create paned window to separate left pane against right pane
panedWindow = ttk.PanedWindow(root, orient=tkinter.HORIZONTAL, width=400, height=300)
noteList = ttk.Frame(root)  # This is the left pane
noteFrame = ttk.Frame(root)  # This is the right pane

# Create the table view and lean everything to the left
columns = ('name')
treeView = ttk.Treeview(noteList, columns=columns, show='headings')
treeView.heading('name', text='Column Name')
treeView.pack(side=tkinter.TOP, expand=True, fill='both')

settingPane = ttk.Frame(noteList, padding=10)  # Create custom frame for settings

# Create a button that can hide or un-hide settings; left pane
settingsBtn = ttk.Button(noteList, image=cogSample, compound=LEFT, command=lambda: settingwidget(settingPane))
settingsBtn.place(relx=0.9, rely=0.95, anchor='se')

# Add settings to settingsPane
fontSizeValue = tkinter.DoubleVar()
lineSpacingValue = tkinter.DoubleVar()



fontSize = ttk.Scale(settingPane,
                     from_=0,
                     to=10,
                     orient='horizontal',
                     command=fontsizechanged,
                     variable=fontSizeValue
                     )

lineSpacing = ttk.Scale(settingPane,
                        from_=0,
                        to=10,
                        orient='horizontal',
                        command=linespacingchanged,
                        variable=lineSpacingValue
                        )



fontSizeLabel = ttk.Label(settingPane, text=getfontsize())
lineSpacingLabel = ttk.Label(settingPane, text=getlinespace())

# Organize setting children widgets
fontSize.grid(row=0, column=0)
fontSizeLabel.grid(row=0, column=1)
lineSpacing.grid(row=1, column=0)
lineSpacingLabel.grid(row=1, column=1)


# Following two for loops populate treeView for testing purposes
contacts = []
for i in range(1, 20):
    contacts.append(str(i))

for contact in contacts:
    treeView.insert('', tkinter.END, values=contact)

# Create a thin loading bar; placed on the top
load = ttk.Progressbar(root, orient='horizontal', mode='determinate')
load.pack(fill='x')

# Create scroll bar for text editable frame; left side
noteScroll = ttk.Scrollbar(treeView, orient=tkinter.VERTICAL, command=treeView.yview)
noteScroll.pack(fill='y', side=tkinter.RIGHT)

# Create ability to scroll through list of notes; right side
text = Text(noteFrame, wrap='word')
scroll = ttk.Scrollbar(noteFrame, orient='vertical')
scroll.config(command=text.yview)
scroll.pack(side=tkinter.RIGHT, fill='y')
text.pack(fill='both', expand=True)  # need to pack text widget last for the scroll attachment

# Pack widgets into PanedWindow
panedWindow.add(noteList)
panedWindow.add(noteFrame)

panedWindow.pack(fill=tkinter.BOTH, expand=True)  # Pack panedWindow

# Create an easy way to allow for resizing to occur, adds 3 dots in bottom right corner
grip = ttk.Sizegrip(root)
grip.pack(side=tkinter.RIGHT)

root.mainloop()
