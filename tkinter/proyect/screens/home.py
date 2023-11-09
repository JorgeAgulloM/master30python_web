### Home Screen ###
from tkinter import Tk, ttk, Frame, Label
from constants.colors import PRIMARY, SECONDARY, TERTIARY, SECONDARY_BLACK, PRIMARY_BLACK
from data.data import products
from data.product_model import NAME, PRICE, AMOUNT, DESCRIPTION

class Home():

    def __init__(self, window: Tk):
        self.bg=SECONDARY
        self.fg='black'
        
        self.window=window
        window.config(
            bg=SECONDARY
        )
        self.frame=Frame(window)
        self.frame.config(bg=self.bg)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid(row=0, column=0, sticky='nsew')

    def main(self):
        self.main_label()
        if self.frame.grid:
            self.frame.grid_remove()
        self.frame.grid(row=0, column=0, sticky='nsew')
        
        height = len(products)
        if height > 30:
            height = 30
        
        table = ttk.Treeview(self.frame, height=height, column=(PRICE, AMOUNT, DESCRIPTION))
        table.grid(row=1, column=0, columnspan=2, padx=8, pady=8, sticky='nsew')
        table.heading('#0', text=NAME, anchor='w')
        table.heading(PRICE, text=PRICE, anchor='w')
        table.heading(AMOUNT, text=AMOUNT, anchor='w')
        table.heading(DESCRIPTION, text=DESCRIPTION, anchor='w')
        
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=table.yview)
        scrollbar.grid(row=1, column=1, sticky='ns')
        table.configure(yscrollcommand=scrollbar.set)
        
        if len(table.get_children()) > 0:
            table.delete(table.get_children()[0])
        
        for product in products:
            table.insert('', 0, text=product[NAME], values=(product[PRICE], product[AMOUNT], product[DESCRIPTION]))
                 
    def remove(self):
        if self.frame.grid:
            self.frame.grid_remove()
            
    def main_label(self):
        label=Label(self.frame)
        label.grid(row=0, column=0)
        label.config(
            bg=self.bg,
            fg=self.fg,
            text='Listado de productos',
            font=('Consolas', 16),
            padx=8,
            pady=8
        )
        label.grid(row=0, column=0)

    def label(self, name:str, row:int, col:int, frame:Frame, is_top:bool) -> Label:
        if is_top:
            label = Label(frame, justify='left', wraplength=450)
            label.grid(row=row, column=col, sticky='new')
        else:
            label = Label(frame, justify='left')
            label.grid(row=row, column=col, sticky='nw')
        
        label.config(
            text=name,
            font=('Consolas', 12),
            fg=self.fg,
            bg=self.bg,
            width=40,
            padx=8,
            pady=8
        )
        return label
            