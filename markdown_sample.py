import tkinter
from tkinter import *
from tkinter import font as tkfont
import re

sampleText = '**Sample** Text. This **bolded**'
boldpattern = re.findall("\*\*[a-zA-z]*\*\*", sampleText)

for i in boldpattern:
    print(i)

root = Tk()


# Initially, not having both lines didn't auto update. Might be a better
# Tkinter doesn't support compiled regular expressions??
def func(event):
    text.tag_add("bolded", '1.0', '1.9')
    text.tag_config("bolded", font=bold_font)


bold_font = tkfont.Font(weight='bold')

text = Text(root)

text.insert(END, '**Text**')
text.insert('1.0', ' Sample')
text.tag_add("bolded", '1.0', '1.9')
text.tag_config("bolded", font=bold_font)
text.bind('<KeyRelease>', func)
text.pack(expand=True, fill='both')

root.mainloop()
