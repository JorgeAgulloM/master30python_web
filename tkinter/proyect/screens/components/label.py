### Label Component ###
from tkinter import Label, Frame

def label(fg:str, bg:str, name:str, row:int, col:int, frame:Frame, is_top:bool) -> Label:
    label = Label(frame)
    if is_top:
        label.grid(row=row, column=col, sticky='nw')
    else:
        label.grid(row=row, column=col, sticky='w')
    label.config(
        text=name,
        font=('Consolas', 12),
        fg=fg,
        bg=bg,
        width=10,
        padx=8,
        pady=8
    )
    return label