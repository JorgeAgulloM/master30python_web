### Add Screen ###
from tkinter import Tk, Frame, Label, Entry, Text, Button, StringVar
from constants.colors import PRIMARY, SECONDARY, TERTIARY, SECONDARY_BLACK, PRIMARY_BLACK
from data.data import products
from data.product_model import product, NAME, PRICE, AMOUNT, DESCRIPTION

class Add():

    def __init__(self, window: Tk):
        self.bg=SECONDARY
        self.fg='black'
        
        self.window=window
        self.frame=Frame(window)
        self.frame.config(bg=self.bg)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid(row=0, column=0, sticky='ew')
        self.value_name = StringVar()
        self.value_price = StringVar()
        self.value_amount = StringVar()
        self.value_description = StringVar()

    def main(self) -> Frame:
        self.head_label()
        self.frame.grid(row=0, column=0, sticky='ew')
        self.form()
        
    def remove(self):
        if self.frame.grid:
            self.frame.grid_remove()
            
    def head_label(self):
        label = Label(self.frame)
        label.grid(row=0, column=0)
        label.config(
            bg=self.bg,
            fg=self.fg,
            text='Añadir Producto',
            font=('Consolas', 16),
            padx=8,
            pady=8
        )
        label.grid(row=0, column=0, sticky='ew')
            
    def form(self):
        self.value_name = self.field('Nombre', 2, True)
        self.value_price = self.field('Precio', 3, True)
        self.value_amount = self.field('Cantidad', 4, True)
        self.value_description = self.field('Descripción', 5, False)
        self.button(6)
    
    def field(self, name:str, row:int, is_entry:bool):
        frame = Frame(self.frame)
        frame.config(
            bg=self.bg
        )
        frame.grid(row=row, column=0, sticky='w')
        self.label(name, row, frame, not is_entry)
        if is_entry:
            return self.entry(row, frame)[1]
        self.text = self.description_text(row, frame)
        return self.text[1]
    
    def label(self, name:str, row:int, frame:Frame, is_top:bool) -> Label:
        label = Label(frame)
        if is_top:
            label.grid(row=row, column=0, sticky='nw')
        else:
            label.grid(row=row, column=0, sticky='w')
        label.config(
            text=name,
            font=('Consolas', 12),
            fg=self.fg,
            bg=self.bg,
            width=10,
            padx=8,
            pady=8
        )
        return label
    
    def entry(self, row:int, frame:Frame) -> [Entry, StringVar]:
        data = StringVar()
        
        entry = Entry(frame)
        entry.grid(row=row, column=1)
        entry.config(
            textvariable=data,
            font=('Consolas', 12),
            width=30
        )
        return [entry, data]
    
    def description_text(self, row:int, frame:Frame) -> [Text, StringVar]:
        data = StringVar()
        frame.config(pady=8)
        text = Text(frame)
        text.config(
            font=('Consolas', 12),
            width=30,
            height=8,
            pady=4   
        )
        text.grid(row=row, column=1)
        
        def update_data():
            data.set(text.get('1.0', 'end-1c'))
            
        text.bind('<KeyRelease>', lambda event: update_data())
        
        return [text, data]
    
    def button(self, row:int) -> Button:
        bt_frame = Frame(self.frame)
        bt_frame.config(
            bg=self.bg,
            padx=16, 
            pady=8
        )
        bt_frame.grid(row=row, column=0, sticky='e')
        
        button = Button(bt_frame, text='Guardar')
        button.config(
            command=self.save_data,
            bg=PRIMARY_BLACK,
            fg='white',
            font=('Consolas', 16),
            padx=8,
            pady=8
        )
        button.grid(row=row, column=0)
        return button
    
    def save_data(self):
        new_product = {}
        new_product[NAME] = self.value_name.get()
        new_product[PRICE] = self.value_price.get()
        new_product[AMOUNT] = self.value_amount.get()
        new_product[DESCRIPTION] = self.value_description.get()
        
        self.value_name.set('')
        self.value_price.set('')
        self.value_amount.set('')
        self.value_description.set('')
        self.text[0].delete('1.0', 'end')
        
        products.append(new_product)
        
        for item in products:
            print(item)
        print('----------------------------------------')