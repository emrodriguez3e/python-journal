import tkinter as tk
from tkinter import ttk

"""
This code was found from here, make sure to change file being used

https://stackoverflow.com/questions/38180388/tkinter-how-to-insert-an-image-to-a-text-widget

"""


# def add_image():
#     # This uses two different methods of image creation.
#     # Original post doesn't use subsampled version
#
#     text.image_create(tk.END, image=img)  # Example 1
#     text.window_create(tk.END, window=tk.Label(text, image=img))  # Example 2

# text = tk.Text(root)
# text.pack(padx=20, pady=20)

# tk.Button(root, text="Insert", command=add_image).pack()
#
# img = tk.PhotoImage(file="img.png")
# img_sub = img.subsample(2, 2)

root = tk.Tk()

c = tk.Canvas(root, height=10)
c.pack()

for i in range(10):
    ttk.Label(c, text='Sample Text').grid(row=i+1, column=1)

s1 = ttk.Scale(c)

s2 = tk.Scrollbar(c, orient='vertical', command=c.yview)

s1.grid(row=0, column=2)



root.mainloop()

