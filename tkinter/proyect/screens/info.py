### Info Screen ###
from tkinter import Tk, Frame, Label
from constants.colors import PRIMARY, SECONDARY, TERTIARY, SECONDARY_BLACK, PRIMARY_BLACK

class Info():

    def __init__(self, window: Tk):
        self.bg=SECONDARY
        self.fg=PRIMARY_BLACK
        
        self.window=window
        window.config(
            bg=SECONDARY
        )
        self.frame=Frame(self.window)
        self.frame.config(bg=self.bg)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid(row=0, column=0, sticky='nsew')
        self.frame.grid(row=0, column=0, sticky='ew')
        
    def main(self) -> Frame:
        self.label('Creado por Jorge Agulló\nsin hacer caso a Victor Robles', 0)
        self.label('Creado con Python y Tkinter', 1)
        self.frame.grid(row=0, column=0, sticky='ew')
        
    def remove(self):
        if self.frame.grid:
            self.frame.grid_remove()
            
    def label(self, text:str, row:int) -> Label:
        label = Label(self.frame)
        label.config(
            text=text,
            fg=self.fg,
            bg=self.bg,
            font=('Consolas', 16),
            padx=24,
            pady=24
        )
        label.grid(row=row, column=0)
        
        return label
      