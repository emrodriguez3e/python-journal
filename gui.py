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


# Allows to change the text of the note
def treeitem(event):
    for item in treeView.selection():
        item = treeView.item(item)
        item = item['text']
        text.delete(0.0, END)
        text.insert(END, item)


# Function meant to help get attributes of widgets
def printhelp(i=0):
    try:
        print(i.configure().keys())
    except:
        print(str(i) + ' is not a valid input. Skipped.\n')


# Load Media
cogSize = 6
cog = PhotoImage(file=r"media/cog.png")
cogSample = cog.subsample(cogSize, cogSize)

# Create paned window to separate left pane against right pane
panedWindow = ttk.PanedWindow(root, orient=tkinter.HORIZONTAL, width=400, height=300)

# Frames for left pane
leftPane = ttk.Frame(root)  # This is the left pane
treeFrame = ttk.Frame(leftPane) # Frame to put into left

settingFrame = ttk.Frame(leftPane)

settingPane = ttk.Frame(settingFrame, padding=10)  # Create custom frame for settings


# Frames for right pane
textFrame = ttk.Frame(root)  # This is the right pane


# Create the table view and lean everything to the left
# columns = ('Column Name')
treeView = ttk.Treeview(treeFrame, columns=('0'), show='headings')
treeView.heading('0', text="Heading Name")
treeView.bind('<<TreeviewSelect>>', treeitem) # This event updates note
treeView.pack(side=tkinter.LEFT, expand=True, fill='both')


# Following code is how the treeview is populated.
for i in range(1, 20):
    treeView.insert('', tkinter.END, text='Body of the text', values=("Note "+str(i), ""))


# Scroll for treeView; left side
noteScroll = ttk.Scrollbar(treeFrame, orient=tkinter.VERTICAL, command=treeView.yview)
noteScroll.pack(fill='y', side=tkinter.RIGHT)

# Create a button that can hide or un-hide settings; left pane
settingsBtn = ttk.Button(leftPane, image=cogSample, compound=LEFT, command=lambda: settingwidget(settingPane))
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


# Loading bar to be placed above w note; right side
load = ttk.Progressbar(root, orient='horizontal', mode='determinate')
load.pack(fill='x')


# Create ability to scroll through list of notes; right side
text = Text(textFrame, wrap='word')  # Text widget


scroll = ttk.Scrollbar(textFrame, orient='vertical')  # Scroll Widget
scroll.config(command=text.yview)
scroll.pack(side=tkinter.RIGHT, fill='y')
text.pack(fill='both', expand=True)  # need to pack text widget last for the scroll attachment


treeFrame.pack(fill='both')

# Pack widgets into PanedWindow
panedWindow.add(leftPane)
panedWindow.add(textFrame)

panedWindow.pack(fill=tkinter.BOTH, expand=True)  # Pack panedWindow

# Create an easy way to allow for resizing to occur, adds 3 dots in bottom right corner
grip = ttk.Sizegrip(root)
grip.pack(side=tkinter.RIGHT)

root.mainloop()
