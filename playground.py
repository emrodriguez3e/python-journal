import tkinter as tk
from tkinter import ttk


"""
This code was found from here, make sure to change file being used

https://stackoverflow.com/questions/38180388/tkinter-how-to-insert-an-image-to-a-text-widget

"""
def add_image():
    # This uses two different methods of image creation.
    # Original post doesn't use subsampled version
    img = tk.PhotoImage(file = r"img2.gif")  # TODO: Make sure to change this!
    img_sub = img.subsample(15,15)
    text.image_create(tk.END, image = img_sub) # Example 1
    #text.window_create(tk.END, window = tk.Label(text, image = img_sub)) # Example 2

root = tk.Tk()

text = tk.Text(root)
text.pack(padx = 20, pady = 20)

tk.Button(root, text = "Insert", command = add_image).pack()



root.mainloop()
