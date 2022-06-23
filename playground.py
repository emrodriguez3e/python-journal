from tkinter import *
from tkinter import ttk

root = Tk()

c = Canvas(height=300, width=500)
c.pack(expand=True, fill='both')

p = PhotoImage(file='media/img.png')
image = c.create_image(50, 50, image=p)

c.create_text((100, 250), text='This is going to be a big sentence', fill='red')

root.mainloop()
