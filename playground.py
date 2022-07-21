import tkinter.ttk
from tkinter import *

# from tkinter.ttk import *

"""
This code was found from here, make sure to change file being used
https://stackoverflow.com/questions/38180388/tkinter-how-to-insert-an-image-to-a-text-widget
"""

def add_image():
    # This uses two different methods of image creation.
    # Original post doesn't use subsampled version

    text.image_create(END, image=img)  # Example 1
    text.window_create(END, window=Label(text, image=img))  # Example 2

root = Tk()
text = Text(root)
text.pack(padx=20, pady=20)

Button(root, text="Insert", command=add_image).pack()

img = PhotoImage(file="img.png")
img_sub = img.subsample(2, 2)

root.mainloop()

