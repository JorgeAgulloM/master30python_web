### Thineter - Creación de apps gráficas para escritorio ###
import tkinter as tk
import os.path as path


class MyFirstProgram():
    
    def __init__(self):
        self.title = 'Interface with Python & Tkinter'
        self.icon = './images/birra.ico'
        self.size = '750x450'
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
        text.pack()
        
    def show(self):
        # Arrancar la ventana
        self.window.mainloop()
                
# Init

program = MyFirstProgram()
program.load()
program.add_text('Hello tkinter!')
program.show()