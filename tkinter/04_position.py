### Textos ###
import tkinter as tk
import os.path as path

class MyFirstProgram():
    
    def __init__(self):
        self.title = 'Interface with Python & Tkinter - Textos'
        self.icon = './images/birra.ico'
        self.size = '750x750'
        self.resizable = False
        
    def load(self):
        # Ventana raiz
        window = tk.Tk()
        self.window = window
        
        # ruta absoluta de icono
        icon_path = path.abspath(self.icon)

        # fabIcon
        window.iconbitmap(icon_path)

        # title
        window.title(self.title)

        # Setear tamaño
        #window.geometry(self.size)

        # Bloquear tamaño de ventana
        if self.resizable:
            window.resizable(1, 1)
        else:
            window.resizable(0, 0) # x, y == 1, 1 permite ambos ejes.
        
    def fixed_text(self, data, color, anchor, side):
        text = tk.Label(self.window, text=data)
        text.config(
            fg='white', # reconoce várias formas de introducción de colores
            bg=color, # como en hexadecimal
            padx=20,
            pady=10,
            font=('Consolas, 16'), # Configura la orientación del texto dentro de su 'caja' # no son pixeles
            cursor='circle'
        )
        text.pack(anchor=anchor, side=side, fill='x') # Configura la orientación de la caja de texto en la ventana 
               
    def add_text(self, data, color, anchor, side):
        text = tk.Label(self.window, text=data)
        text.config(
            fg='white', # reconoce várias formas de introducción de colores
            bg=color, # como en hexadecimal
            padx=20,
            pady=10,
            font=('Consolas, 16'),
            anchor=anchor, # Configura la orientación del texto dentro de su 'caja'
            width=10, # no son pixeles
            cursor='circle'
        )
        text.pack(side=side, fill='x', expand='yes') # Configura la orientación de la caja de texto en la ventana
        
    def text_test(self, name: str, surname: str, country: str):
        return f'Hola {name} {surname}, parece que eres de {country}'
        
    def show(self):
        # Arrancar la ventana
        self.window.mainloop()
                
# Init

program = MyFirstProgram()
program.load()
program.fixed_text('Hello tkinter!', 'black', 'ne', 'top')
program.fixed_text('This is Yorch', 'orange', 'ne', 'top')
program.add_text('Basic', 'blue', 'n', 'left')
program.add_text('Basic', 'green', 'e', 'left')
program.add_text('Basic', 'red', 's', 'left')
program.show()
