from tkinter import *
from tkinter import ttk
root = Tk()
# root.geometry("500x500") // set the size sa window

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello from Group 2!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0) // adds quit botton
root.mainloop()
