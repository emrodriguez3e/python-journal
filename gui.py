import time
import tkinter
from tkinter import *
from tkinter import ttk
import os
from tkinter import font as tkfont


# Create root
root = Tk()
root.title("Python Journal")  # Label the window
root.resizable(True, True)

# Initial width and height dimensions
w = 600
h = 500

# Get screen info
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# Calculate x and y for Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.minsize(width=450, height=250)

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
    if not os.path.isdir('noteDirectory'):
        os.mkdir('noteDirectory')
    note_directory = os.path.join(os.getcwd(), 'noteDirectory')

    #This is where textframe is added to the frame but isn't packed?
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


# Function that creates popup menu in treeView at cursor. Doesn't work on MacOS
def tree_view_pop_up(event):
    treeView.selection_set(treeView.identify_row(event.y)) #changes focus to right clicked item
    try:
        treeViewRightClick.tk_popup(event.x_root, event.y_root)
    finally:
        treeViewRightClick.grab_release()


def tree_view_pop_up_duplicate():
    # Get body of selected note
    file = open('noteDirectory/'+treeView.item(treeView.selection())['values'][0],'r')
    copy = file.read()
    file.close()

    #Duplicate that note
    file_name = treeView.item(treeView.selection())['values'][0].replace('.txt', '') + ' copy.txt'
    row_id = treeView.index(treeView.selection())
    file = open('noteDirectory/'+ file_name,'w')
    body = 'This is a new note'
    file.write(body)
    file.close()

    # insert note after duplicated note
    treeView.insert('', row_id, text=copy, values=(file_name,''))



def tree_view_pop_up_delete():
    os.remove('noteDirectory/' + treeView.item(treeView.selection())['values'][0])  # goes out of range
    treeView.delete(treeView.selection())

def tree_view_pop_up_rename():
    pass

def tree_view_debug(event):
    i = treeView.item(treeView.selection())
    print(len(i['text'].split()))



# Function that creates popup menu in note view at cursor. MacOS works
def note_pop_up(event):
    try:
        noteRightClick.tk_popup(event.x_root, event.y_root)
    finally:
        noteRightClick.grab_release()


# This functions opens up and gets all available files. Should rename to tree_read
def tree_fill():
    if not os.path.isdir('noteDirectory'):
        os.mkdir('noteDirectory')
    else:
        pass

    # TODO: Should create a list of files to ignore. Could cause some issues in the future
    for i in os.listdir('noteDirectory'):
        if not i == '.DS_Store':
            file = open('noteDirectory/' + i, 'r')
            treeView.insert('', tkinter.END, text=file.read(), values=(i, ""))
            file.close()


def create_new_note():

    # if there is no note in the directory
    if len(treeView.get_children()) == 0:
       newest_note = 'untitled1.txt'

    # Gets biggest note number
    else:
        for i in treeView.get_children():
            if 'untitled' in treeView.item(i)['values'][0] and not 'copy' in treeView.item(i)['values'][0]:
                note_name = treeView.item(i)['values'][0].replace('untitled', '')
                note_name = note_name.replace('.txt', '')

        newest_note = 'untitled'+str(int(note_name)+1)+'.txt'
    file = open('noteDirectory/'+newest_note,'w')
    body = 'This is a new note'
    file.write(body)
    file.close()
    treeView.insert('', tkinter.END, text=body, values=(newest_note, ""))


# Updates GUI strings by reading txt string
def update_note(event):
    new_string = text.get("1.0", "end-1c")
    row_id = treeView.index(treeView.focus())
    file = open('noteDirectory/untitled' + str(row_id) + '.txt', 'w+')
    file.write(new_string)
    treeView.item(item=treeView.selection(), text=new_string)
    file.close()


# Attempt to perform markdown formatting here, currently not being used.
def formatter(event):
    start = '1.0'
    end = 'end'
    text.tag_add('', '1.0', 'end')


# Function meant to help get attributes of widgets
def print_help(i=None):
    try:
        print(i.configure().keys())
    except:
        print(str(i) + ' is not a valid input. Skipped.\n')


# Load Media
mediaSize = 6
cog = PhotoImage(file=r"media/cog.png")
cogSample = cog.subsample(mediaSize, mediaSize)

plus = PhotoImage(file=r"media/plus.png")
plusSample = plus.subsample(mediaSize * 2, mediaSize * 2)

# Create paned window to separate left pane against right pane
panedWindow = ttk.PanedWindow(root, orient=tkinter.HORIZONTAL)

# Frames for left pane
leftPane = ttk.Frame(root, padding=2)  # This is the left pane
topLeftPane = ttk.Frame(leftPane)
treeFrame = ttk.Frame(leftPane)  # Frame to put top into left

settingFrame = ttk.Frame(leftPane)  # Frame to put into bottom left
settingPane = ttk.Frame(settingFrame, padding=10)  # Frame to put into settingFrame

# Frames for right pane
textFrame = ttk.Frame(root)  # This is the right pane
infoFrame = ttk.Frame(textFrame)

root.bind('<Alt-d>', tree_view_debug)

# Right click menu
treeViewRightClick = Menu(root, tearoff=0)
treeViewRightClick.add_command(label='Duplicate', command=tree_view_pop_up_duplicate)
treeViewRightClick.add_command(label='Delete', command=tree_view_pop_up_delete)
treeViewRightClick.add_command(label='Rename File')
treeViewRightClick.add_separator()
treeViewRightClick.add_command(label='Info', command=tree_view_debug)

# bear has the following options
'''
Open in a new window
Copy as
Pin/unpin note
Archive
Privacy
Merge
'''

# Create the table view and lean everything to the left
# columns = ('Column Name')
treeView = ttk.Treeview(treeFrame, columns='0', show='headings')
treeView.heading('0', text="Notes")
treeView.bind('<<TreeviewSelect>>', tree_item)  # This event updates note
treeView.bind('<Button-3>', tree_view_pop_up)  # bind treeViewRightClick here
treeView.bind('<Button-2>', tree_view_pop_up)
treeView.bind('<Option-Button-1>', tree_view_pop_up)

treeView.pack(side=tkinter.LEFT, expand=True, fill='both')

# This is going to be used to call to create necessary directory and fill treeView
tree_fill()

# Scroll for treeView; left side
noteScroll = ttk.Scrollbar(treeFrame, orient=tkinter.VERTICAL, command=treeView.yview)
noteScroll.pack(fill='y', side=tkinter.RIGHT)

# This section should be above the tree
newNote = ttk.Button(topLeftPane, compound=LEFT, image=plusSample, command=create_new_note)  # new note button
newNote.pack(side=tkinter.RIGHT)

searchField = Entry(topLeftPane)  # search field
searchField.pack(side=tkinter.RIGHT)

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

fontSizeText = ttk.Label(settingPane, text='Font Size ')
fontSizeLabel = ttk.Label(settingPane, text=get_font_size())

lineSpaceText = ttk.Label(settingPane, text='Line Spacing ')
lineSpacingLabel = ttk.Label(settingPane, text=get_line_space())

# Organize setting children widgets
fontSizeText.grid(row=0, column=0)
fontSize.grid(row=0, column=1)
fontSizeLabel.grid(row=0, column=2)

lineSpaceText.grid(row=1, column=0)
lineSpacing.grid(row=1, column=1)
lineSpacingLabel.grid(row=1, column=2)

topLeftPane.pack(fill='x', side=tkinter.TOP)
settingPane.pack(fill='x', side=tkinter.BOTTOM)
treeFrame.pack(expand=True, fill='both')

# Loading bar to be placed above w note; right side
load = ttk.Progressbar(root, orient='horizontal', mode='determinate')
load.pack(fill='x')

# Right click menu for notes, does nothing at the moment
noteRightClick = Menu(root, tearoff=0)
noteRightClick.add_command(label='Cut')
noteRightClick.add_command(label='Copy')
noteRightClick.add_command(label='Paste')
noteRightClick.add_separator()
noteRightClick.add_command(label='Bold')
noteRightClick.add_command(label='Italics')
noteRightClick.add_command(label='Underline')

# Create ability to scroll through list of notes; right side
text = Text(textFrame, wrap='word')  # Text widget
text.tag_configure("bold", font=(bold_font))
text.bind('<KeyRelease>', update_note)  # Command will call function after every
text.bind('<Button-3>', note_pop_up)
text.bind('<Button-2>', note_pop_up)
text.bind('<Option-Button-1>', note_pop_up)  # Pop up menu doesn't work on mac for some reason
text.configure()

# infoFrame informatino; right side
word_count = Label(infoFrame, text='Word Count\n0', padx=10)
word_count.pack()

character_count =Label(infoFrame, text='Char Count\n0')
character_count.pack()

infoFrame.pack(fill='y', expand=False, side=tkinter.RIGHT) #text pack needs to be last

scroll = ttk.Scrollbar(textFrame, orient='vertical')  # Scroll Widget
scroll.config(command=text.yview)
scroll.pack(side=tkinter.RIGHT, fill='y')
text.pack(fill='both',expand=True, side=tkinter.LEFT)  # need to pack text widget last for the scroll attachment


# Pack widgets into PanedWindow
panedWindow.add(leftPane)


panedWindow.pack(fill=tkinter.BOTH, expand=True)  # Pack panedWindow

# Create an easy way to allow for resizing to occur, adds 3 dots in bottom right corner
grip = ttk.Sizegrip(root)
grip.pack(side=tkinter.RIGHT)

root.mainloop()