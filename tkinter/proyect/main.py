from tkinter import Tk, Label
from menu import MainMenu
from screens.home import Home

window = Tk()
window.geometry('400x600')
window.title('Proyecto COSA - Con Tkinter y Python')
window.resizable(0, 0)

main_menu = MainMenu(window)
window.config(menu=main_menu.menu())
window.grid_columnconfigure(0, weight=1)

window.mainloop()
