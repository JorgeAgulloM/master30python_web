from tkinter import Tk, Button, messagebox

window = Tk()
window.config(bd=70)

def show_info():
    messagebox.showinfo('Ojo Cuidaooo!! Info', 'Esto es una ventana de info')
def show_warning():
    messagebox.showwarning('Ojo Cuidaooo!! Waring', 'Esto es una ventana de warning')
def show_error():
    messagebox.showerror('Ojo Cuidaooo!! Error', 'Esto es una ventana de error')
def show_alert_exit(username: str):
    result = messagebox.askquestion('Salir', f'¿Quieres salir {username}?')
    if result == 'yes':
        messagebox.showinfo('Saliendo', 'Adios!!')
        window.destroy()

Button(window, text='Mostrar Info', command=show_info).pack()
Button(window, text='Mostrar Warning', command=show_warning).pack()
Button(window, text='Mostrar Error', command=show_error).pack()
Button(window, text='Salir', command=lambda:show_alert_exit('Jorge')).pack()

window.mainloop()