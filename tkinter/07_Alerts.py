from tkinter import Tk, Button, messagebox

window = Tk()
window.config(bd=70)

def show_info():
    messagebox.showinfo('Ojo Cuidaooo!! Info', 'Esto es una ventana de info')
def show_warning():
    messagebox.showwarning('Ojo Cuidaooo!! Waring', 'Esto es una ventana de warning')
def show_error():
    messagebox.showerror('Ojo Cuidaooo!! Error', 'Esto es una ventana de error')
def show_alert_exit():
    result = messagebox.askquestion('Salir', '¿Quieres salir?')
    if result == 'yes':
        window.destroy()

Button(window, text='Mostrar Info', command=show_info).pack()
Button(window, text='Mostrar Warning', command=show_warning).pack()
Button(window, text='Mostrar Error', command=show_error).pack()
Button(window, text='Salir', command=show_alert_exit).pack()

window.mainloop()