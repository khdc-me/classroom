import tkinter as tk
from tkinter import ttk


def change_label_aLabel_text():
    btn_action.configure(text="** I have been clicked! **" + name.get())
    lbl_aLabel.configure(foreground="red")
    lbl_aLabel.configure(text="A red label.")

win = tk.Tk()
win.title("First Python GUI")
#win.resizable(False, False)
lbl_aLabel = ttk.Label(win, text="A Label")
btn_action = ttk.Button(win, text="Click Me!", command=change_label_aLabel_text)
name = tk.StringVar()
txt_name = ttk.Entry(win, width=12, textvariable=name)

lbl_aLabel.grid(column=0, row=0)
btn_action.grid(column=1, row=0)
txt_name.grid(column=0, row=1)

win.mainloop()