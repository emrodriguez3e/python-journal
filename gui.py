import tkinter
from tkinter import *
from tkinter import ttk
import os
from tkinter import font as tkfont

# Create root
root = Tk()
root.title("Python Journal")  # Label the window
root.resizable(True, True)
root.geometry('500x400')
root.minsize(width=450, height=300)


bold_font = tkfont.Font(weight='bold')

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

    noteDirectory = os.path.join(os.getcwd(), 'noteDirectory')

    try:
        panedWindow.forget(textFrame)
    except:
        print('Pane could not be forgotten')

    for item in treeView.selection():
        item = treeView.item(item)
        item = item['text']
        text.delete(0.0, END)
        text.insert(END, item)

        # file = open(noteDirectory+"untitled"+".txt")
        #
        # file.close()
    panedWindow.add(textFrame)


def get_note_body():
    pass

def tree_fill():
    note_directory = os.path.join(os.getcwd(), 'noteDirectory')

    if not os.path.isdir(note_directory):
        os.mkdir(note_directory)
    else:
        file = open('noteDirectory/untitled0.txt', 'w')
        file.write('Untitled document 0')
        file.close()

        file = open('noteDirectory/untitled1.txt', 'w')
        file.write('Untitled document 1')
        file.close()

    list_amount = len(os.listdir(note_directory))

    for j in range(0, list_amount-1):
        file = open('noteDirectory/untitled'+str(j)+'.txt')
        treeView.insert('', tkinter.END, text=file.read(), values=("Note", ""))
        file.close()


def save_note():
    # Need to be able to check if the file exists
    # If it is, then simply save the text string from the body
    # But I also need to figure out how to name the note tho
    file = open('noteDirectory/untitled.txt', 'w')
    file.close()


def update_note():
    new_string = text.get("1.0", "end-1c")


def format(event):
    start = '1.0'
    end='end'
    text.tag_add('', '1.0','end')



# Function meant to help get attributes of widgets
def print_help(i=None):
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
treeFrame = ttk.Frame(leftPane)  # Frame to put top into left

settingFrame = ttk.Frame(leftPane)  # Frame to put into bottom left

settingPane = ttk.Frame(settingFrame, padding=10)  # Frame to put into settingFrame


# Frames for right pane
textFrame = ttk.Frame(root)  # This is the right pane


# Create the table view and lean everything to the left
# columns = ('Column Name')
treeView = ttk.Treeview(treeFrame, columns='0', show='headings')
treeView.heading('0', text="")
treeView.bind('<<TreeviewSelect>>', tree_item)  # This event updates note
treeView.pack(side=tkinter.LEFT, expand=True, fill='both')


# This is going to be used to call to create necessary directory and fill treeView
tree_fill()


# Scroll for treeView; left side
noteScroll = ttk.Scrollbar(treeFrame, orient=tkinter.VERTICAL, command=treeView.yview)
noteScroll.pack(fill='y', side=tkinter.RIGHT)

newBtn = ttk.Button(leftPane, compound=LEFT)
newBtn.pack()

# Create a button that can hide or un-hide settings; left pane
settingsBtn = ttk.Button(leftPane, image=cogSample, compound=LEFT, command=lambda: settings_widget(settingFrame))
settingsBtn.place(relx=0.9, rely=0.95, anchor='se')

# Add settings to settingsPane
fontSizeValue = tkinter.DoubleVar()
lineSpacingValue = tkinter.DoubleVar()



fontSize = ttk.Scale(settingPane,
                     from_=10,
                     to=24,
                     orient='horizontal',
                     command=font_size_changed,
                     variable=fontSizeValue
                     )

lineSpacing = ttk.Scale(settingPane,
                        from_=10,
                        to=24,
                        orient='horizontal',
                        command=line_spacing_changed,
                        variable=lineSpacingValue,
                        )

print_help(lineSpacing)



fontSizeLabel = ttk.Label(settingPane, text=get_font_size())
lineSpacingLabel = ttk.Label(settingPane, text=get_line_space())

# Organize setting children widgets
fontSize.grid(row=0, column=0)
fontSizeLabel.grid(row=0, column=1)
lineSpacing.grid(row=1, column=0)
lineSpacingLabel.grid(row=1, column=1)

settingPane.pack(fill='x', side=tkinter.BOTTOM)

# Loading bar to be placed above w note; right side
load = ttk.Progressbar(root, orient='horizontal', mode='determinate')
load.pack(fill='x')

# Create ability to scroll through list of notes; right side
# TODO: Need to figure out how to save the text from the body
text = Text(textFrame, wrap='word')  # Text widget
text.tag_configure("bold", font=(bold_font))
text.bind('<KeyRelease>', format)  # Command will call function after every
text.configure()

scroll = ttk.Scrollbar(textFrame, orient='vertical')  # Scroll Widget
scroll.config(command=text.yview)
scroll.pack(side=tkinter.RIGHT, fill='y')
text.pack(fill='both', expand=True)  # need to pack text widget last for the scroll attachment

treeFrame.pack(expand=True, fill='both', side=tkinter.TOP)

# Pack widgets into PanedWindow
panedWindow.add(leftPane)
# panedWindow.add(textFrame)

panedWindow.pack(fill=tkinter.BOTH, expand=True)  # Pack panedWindow

# Create an easy way to allow for resizing to occur, adds 3 dots in bottom right corner
grip = ttk.Sizegrip(root)
grip.pack(side=tkinter.RIGHT)

root.mainloop()
