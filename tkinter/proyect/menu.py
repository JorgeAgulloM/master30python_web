### Menu ###
from tkinter import Tk, Menu
from screens.home import Home
from screens.add import Add
from screens.info import Info
from constants.colors import PRIMARY, SECONDARY, TERTIARY, SECONDARY_BLACK, PRIMARY_BLACK

class MainMenu():

    def __init__(self, window: Tk):
        self.window = window
        self.home = Home(window)
        self.add = Add(window)
        self.info = Info(window)

    def menu(self) -> Menu:
        main_menu = Menu(self.window)
        main_menu.add_command(label='Inicio', command=lambda:self.change_frame(0))
        main_menu.add_command(label='Añadir', command=lambda:self.change_frame(1))
        main_menu.add_command(label='Información', command=lambda:self.change_frame(2))
        main_menu.add_command(label='Salir', command=main_menu.quit)
        main_menu.config(bg=SECONDARY_BLACK)
        
        self.change_frame(0)
        
        return main_menu

    def change_frame(self, item: int):
        if item == 0:
            self.add.remove()
            self.info.remove()
            return self.home.main()
        
        if item == 1:
            self.home.remove()
            self.info.remove()
            return self.add.main()
        
        if item == 2:
            self.home.remove()
            self.add.remove()
            return self.info.main()

