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
########################################################################################################################

#Following code snippet doesn't work but is much closer to what I need I believe
#https://stackoverflow.com/questions/7727804/tkinter-using-scrollbars-on-a-canvas

root = Tk()

container = Frame(root)
canvas = Canvas(container)
#setting_panel = Frame(canvas)


sample_text = Text(canvas, width=40, height=10, wrap='word')
sample_text.pack(pady=5, expand=False)


font_label = Label(canvas, text='Font Label')
font_scale = ttk.Scale(canvas, orient=HORIZONTAL)

font_label.pack(after=sample_text)
font_scale.pack(after=sample_text)

line_label = Label(canvas, text='Line Label')
line_scale = ttk.Scale(canvas, orient=HORIZONTAL)

line_label.pack(after=sample_text)
line_scale.pack(after=sample_text)



scroll = Scrollbar(container, orient='vertical', command=canvas.yview)
scroll.pack(fill='y', side=RIGHT)

#canvas.configure(yscrollcommand=scroll.set, scrollregion=canvas.bbox('all'))

container.pack()
canvas.pack(expand=True)
#setting_panel.pack()

root.geometry('200x200')
root.mainloop()

