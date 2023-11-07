### Form Avanzado ###
from tkinter import Tk, Label, IntVar, StringVar, W, Checkbutton, Radiobutton, OptionMenu

window = Tk()
window.geometry('800x500')

header = Label(window, text='Formularios 2 con Tkinter y Python')
header.config(
    padx=8,
    pady=8,
    fg='white',
    bg='green',
    font=('Consolas', 16)
)
header.grid(row=0, column=0, columnspan=6, sticky=W)


cb_text_hate = 'Odiar a Victor Robles'
cb_text_tkinter = 'Aprender Tkinter con Python'
cb_hate = IntVar()
cb_tkinter = IntVar()

show = Label(window)
show.grid(row=4, column=0, sticky=W)

def show_state():
    result = ''
    if cb_hate.get():
        result = cb_text_hate
        
    if cb_tkinter.get():
        if cb_hate.get():
            result += f' y {cb_text_tkinter}'
        else:
            result += cb_text_tkinter
        
    if not cb_hate.get() and not cb_tkinter.get():
        result = ''
        
    show.config(text=result)
    

# CheckBox
Label(window, text='¿Que estás haciendo?').grid(row=1, column=0, sticky=W)
Checkbutton(
    window, 
    text=cb_text_hate,
    variable=cb_hate,
    onvalue=1,
    offvalue=0,
    command=show_state
).grid(row=2, column=0, sticky=W)
Checkbutton(
    window, 
    text=cb_text_tkinter,
    variable=cb_tkinter,
    onvalue=1,
    offvalue=0,
    command=show_state
).grid(row=3, column=0, sticky=W)

# RadioButton

def select_option():
    check.config(text=option.get())

option = StringVar()
option.set(None)

Label(window, text='¿Cuas es tu genero?').grid(row=5, column=0, sticky=W)
Radiobutton(
    window, 
    text='Masculino',
    value='Masculino', 
    variable=option, 
    command=select_option
).grid(row=6, column=0, sticky=W)
Radiobutton(
    window, 
    text='Femenino',
    value='Femenino', 
    variable=option, 
    command=select_option
).grid(row=7, column=0, sticky=W)

check = Label(window)
check.grid(row=8, column=0, sticky=W)


# Option Menu
option = StringVar()
option.set('Option1')

Label(window, text='Selecciona una Opción').grid(row=10, column=0, sticky=W)
select = OptionMenu(
    window, 
    option,
    'Opción 1',
    'Opción 2',
    'Opción 3',
    'Opción 4',
    'Opción 5',
)
select.grid(row=11, column=0, sticky=W)

window.mainloop()
