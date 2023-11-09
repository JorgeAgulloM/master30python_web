from tkinter import Tk, Label
from menu import MainMenu
from screens.home import Home

window = Tk()
#window.geometry('400x600')
window.minsize(500, 500)
window.title('Proyecto COSA - Con Tkinter y Python')
window.resizable(1, 1)

main_menu = MainMenu(window)
window.config(menu=main_menu.menu())
window.grid_columnconfigure(0, weight=1)

window.mainloop()
