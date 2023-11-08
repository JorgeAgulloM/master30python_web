### Info Screen ###
from tkinter import Tk, Frame, Label

class Info():

    def __init__(self, window: Tk):
        self.window=window
        self.label = Label(self.window)
        self.label.grid(row=0, column=0)

    def main(self) -> Frame:
        self.label.config(
            text='Información',
            fg='white',
            bg='green',
            font=('Consolas', 30),
            padx=24,
            pady=24
        )
        self.label.grid(row=0, column=0)
        
    def remove(self):
        if self.label.grid:
            self.label.grid_remove()
      