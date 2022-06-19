import tkinter
from tkinter import *
from tkinter import font as tkfont
import re

root = Tk()

bold_font = tkfont.Font(weight='bold')


# Initially, not having both lines didn't auto update. Might be a better
# Tkinter doesn't support compiled regular expressions??
def func(event):
    start_position = '1.0'
    count_var = StringVar()

    while start_position != 'end':
        pos = text.search("\*\*[a-zA-Z]+\*\*", start_position, nocase=1, stopindex='end', regexp=True, count=count_var)
        start_position = '%s + %sc' % (pos, int(count_var.get()) + 1)
        print(start_position)
        text.tag_add('bold_font', pos, start_position)  # Throw a 'bad text index "" here. Doesn't crash program tho'
        text.tag_config('bold_font', font=bold_font)

    print("Position: " + pos + "\nCount: " + count_var.get())


text = Text(root)

text.insert(END, "This is **awesome** stuff to **code**")
# text.tag_add("bolded", '1.0', '1.9')
# text.tag_config("bolded", font=bold_font)
text.bind('<KeyRelease>', func)
text.pack(expand=True, fill='both')

root.mainloop()
