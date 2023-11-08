### Add Screen ###
from tkinter import Tk, Frame, Label, Entry
from constants.colors import PRIMARY, SECONDARY, TERTIARY, SECONDARY_BLACK, PRIMARY_BLACK

class Add():

    def __init__(self, window: Tk):
        self.window=window
        self.frame=Frame(window)
        self.frame.config(bg=SECONDARY)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid(row=0, column=0, sticky='ew')

    def main(self) -> Frame:
        label = Label(self.frame)
        label.grid(row=0, column=0)
        label.config(
            text='Añadir Producto',
            font=('Consolas', 16),
            padx=8,
            pady=8
        )
        label.grid(row=0, column=0, sticky='ew')
        self.frame.grid(row=0, column=0, sticky='ew')
        self.form()
        
    def remove(self):
        if self.frame.grid:
            self.frame.grid_remove()
            
    def form(self):
        self.field('Nombre del producto', 2)
    
    def field(self, name:str, row:int):
        frame = Frame(self.frame)
        frame.grid(row=row, column=0)
        self.label(name, row, frame)
        self.entry(name, row, frame)
        
    
    def label(self, name:str, row:int, frame:Frame) -> Label:
        label = Label(frame)
        label.grid(row=row, column=0)
        label.config(
            text=name,
            font=('Consolas', 8),
            padx=8,
            pady=8
        )
        return label
    
    def entry(self, name:str, row:int, frame:Frame) -> Entry:
        entry = Entry(frame)
        entry.grid(row=row, column=1)
        entry.config(
            text=name,
            font=('Consolas', 8)
        )
        return entry
        