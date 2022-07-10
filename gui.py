from tkinter import *

"""
This file is for creating the gui from the top level
All modules make calls based on their relativity
"""

root = Tk()
root.title('Python Journal')
w = 550
h = 350

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/4) - (w/2)
y = (hs/3) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set loading position
root.minsize(width=450, height=300)  # set minimum window size
paneModule = __import__('PanedWindow')
p_Module = paneModule.paneWindow()

root.mainloop()


