### Textos ###
import tkinter as tk
import os.path as path

class MyFirstProgram():
    
    def __init__(self):
        self.title = 'Interface with Python & Tkinter - Textos'
        self.icon = './images/birra.ico'
        self.size = '750x500'
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
        window.geometry(self.size)

        # Bloquear tamaño de ventana
        if self.resizable:
            window.resizable(1, 1)
        else:
            window.resizable(0, 0) # x, y == 1, 1 permite ambos ejes.
        
    def add_text(self, data):
        text = tk.Label(self.window, text=data)
        text.config(
            fg='white', # reconoce várias formas de introducción de colores
            bg='#000000', # como en hexadecimal
            padx=20,
            pady=10,
            font=('Consolas, 16'),
            anchor='e', # Configura la orientación del texto dentro de su 'caja'
            width=50, # no son pixeles
            cursor='circle'
        )
        text.pack(anchor='w') # Configura la orientación de la caja de texto en la ventana
        
    def text_test(self, name: str, surname: str, country: str):
        return f'Hola {name} {surname}, parece que eres de {country}'
        
    def show(self):
        # Arrancar la ventana
        self.window.mainloop()
                
# Init

program = MyFirstProgram()
program.load()
program.add_text('Hello tkinter!')
program.add_text(program.text_test(name='Jorge', surname='Agulló', country='España'))
program.show()
