from tkinter import *

root = Tk()
root.title('Python Journal')
w = 300
h = 200

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set loading position
root.minsize(width=450, height=250)  # set minimum window size
paneModule = __import__('PanedWindow')
paneModule.paneWindow()
root.mainloop()


