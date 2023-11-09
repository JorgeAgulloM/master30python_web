### Thineter - Creación de apps gráficas para escritorio ###
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry('1280x650')
# Imagen
image = Image.open('./images/goku.jpg')
render = ImageTk.PhotoImage(image)
tk.Label(window, image=render).pack(anchor='center')
window.mainloop()
