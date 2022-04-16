import tkinter
from tkinter import *
from tkinter import ttk

size = 10
root = Tk()
root.geometry('300x300')
c = Canvas(root)

cog = PhotoImage(file=r"media/cog.png")
cogSample = cog.subsample(size,size)

button = ttk.Button(root, image=cogSample, compound=LEFT)

oval = c.create_oval(50, 50, 0, 0, fill="red")



button.place(relx=0.5, rely=0.5)
c.place(relx=0.5, rely=0.5)


root.mainloop()