import tkinter
from tkinter import *
from tkinter import ttk
import os

# Create root
root = Tk()
root.title("Python Journal")  # Label the window
root.resizable(True, True)


def settings_widget(widget):
    # Need to see if the widget is present or not
    # If 1, then it is visible
    if widget.winfo_ismapped() == 1:
        widget.pack_forget()
    else:
        widget.pack()


def get_font_size():
    return '{: .2f}'.format(fontSizeValue.get())


def get_line_space():
    return '{: .2f}'.format(lineSpacingValue.get())


def line_spacing_changed(event):
    lineSpacingLabel.configure(text=get_line_space())


def font_size_changed(event):
    fontSizeLabel.configure(text=get_font_size())


# Allows to change the text of the note
def tree_item(event):
    for item in treeView.selection():
        item = treeView.item(item)
        item = item['text']
        text.delete(0.0, END)
        text.insert(END, item)


def tree_fill():
    note_directory = os.path.join(os.getcwd(), 'noteDirectory')

    if not os.path.isdir(note_directory):
        os.mkdir(note_directory)
    else:
        file = open('noteDirectory/untitled.txt', 'w')
        file.close()

        file = open('noteDirectory/untitled1.txt', 'w')
        file.close()

    list_amount = len(os.listdir(note_directory))

    for j in range(0, list_amount):
        treeView.insert('', tkinter.END, text='Body of the text', values=("Note", ""))


def save_note():
    # Need to be able to check if the file exists
    # If it is, then simply save the text string from the body
    # But I also need to figure out how to name the note tho
    file = open('noteDirectory/untitled.txt', 'w')
    file.close()


def update_note():
    pass


# Function meant to help get attributes of widgets
def print_help(i=0):
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
treeFrame = ttk.Frame(leftPane)  # Frame to put into left

settingFrame = ttk.Frame(leftPane)

settingPane = ttk.Frame(settingFrame, padding=10)  # Create custom frame for settings

# Frames for right pane
textFrame = ttk.Frame(root)  # This is the right pane

# Create the table view and lean everything to the left
# columns = ('Column Name')
treeView = ttk.Treeview(treeFrame, columns=('0'), show='headings')
treeView.heading('0', text="Heading Name")
treeView.bind('<<TreeviewSelect>>', tree_item)  # This event updates note
treeView.pack(side=tkinter.LEFT, expand=True, fill='both')


# This is going to be used to call
tree_fill()


# Scroll for treeView; left side
noteScroll = ttk.Scrollbar(treeFrame, orient=tkinter.VERTICAL, command=treeView.yview)
noteScroll.pack(fill='y', side=tkinter.RIGHT)


# Create a button that can hide or un-hide settings; left pane
settingsBtn = ttk.Button(leftPane, image=cogSample, compound=LEFT, command=lambda: settings_widget(settingPane))
settingsBtn.place(relx=0.9, rely=0.95, anchor='se')

# Add settings to settingsPane
fontSizeValue = tkinter.DoubleVar()
lineSpacingValue = tkinter.DoubleVar()

fontSize = ttk.Scale(settingPane,
                     from_=0,
                     to=10,
                     orient='horizontal',
                     command=font_size_changed,
                     variable=fontSizeValue
                     )

lineSpacing = ttk.Scale(settingPane,
                        from_=0,
                        to=10,
                        orient='horizontal',
                        command=line_spacing_changed,
                        variable=lineSpacingValue
                        )

fontSizeLabel = ttk.Label(settingPane, text=get_font_size())
lineSpacingLabel = ttk.Label(settingPane, text=get_line_space())

# Organize setting children widgets
fontSize.grid(row=0, column=0)
fontSizeLabel.grid(row=0, column=1)
lineSpacing.grid(row=1, column=0)
lineSpacingLabel.grid(row=1, column=1)

# Loading bar to be placed above w note; right side
load = ttk.Progressbar(root, orient='horizontal', mode='determinate')
load.pack(fill='x')

# Create ability to scroll through list of notes; right side
# TODO: Need to figure out how to save the text from the body
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
