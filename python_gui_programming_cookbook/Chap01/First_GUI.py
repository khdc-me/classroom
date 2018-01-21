import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("First Python GUI")
#win.resizable(False, False)
ttk.Label(win, text="A Label").grid(column=0, row=0)

win.mainloop()