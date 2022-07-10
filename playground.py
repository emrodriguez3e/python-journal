import tkinter as tk
import tkinter.ttk as ttk

class App(ttk.Frame):

    def __init__(self, parent=None, *args, **kwargs):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        # Create Treeview
        self.tree = ttk.Treeview(self, column=('A'), selectmode='none', height=7)
        self.tree.grid(row=0, column=0, sticky='nsew')

        # Setup column heading
        self.tree.heading('#0', text=' Pic directory', anchor='center')

        # Insert image to #0
        self._img = tk.PhotoImage(file="media/pin.png") #change to your file path
        self._img_sub = self._img.subsample(47,47)
        self.tree.insert('', 'end', text=" #0's text", image=self._img_sub,
                         value=("A's value", "B's value"))


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('450x180+300+300')

    app = App(root)
    app.grid(row=0, column=0, sticky='nsew')

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    root.mainloop()