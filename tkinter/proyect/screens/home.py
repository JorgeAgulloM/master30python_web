### Home Screen ###
from tkinter import Tk, Frame, Label
from constants.colors import PRIMARY, SECONDARY, TERTIARY, SECONDARY_BLACK, PRIMARY_BLACK

class Home():

    def __init__(self, window: Tk):
        self.window=window
        window.config(
            bg=SECONDARY
        )
        self.frame=Frame(window)
        self.frame.grid(row=0, column=0)

    def main(self):
        label=Label(self.frame)
        label.grid(row=0, column=0)
        label.config(
            text='Inicio',
            fg='white',
            bg='black',
            font=('Consolas', 30),
            padx=24,
            pady=24
        )
        label.grid(row=0, column=0)
        self.frame.grid(row=0,column=0)
        
    def remove(self):
        if self.frame.grid:
            self.frame.grid_remove()
        