import tkinter as tk

window = tk.Tk()
window .geometry('700x400')
window.title('Forms with Tkinter')

# Headline
headline = tk.Label(window, text='Formulario con tkinter')
headline.config(
    fg='white',
    bg='darkgray',
    font=('Consolas', 16),
    padx=8,
    pady=8
)
headline.grid(row=0, column=0, padx=8, pady=8, columnspan=2)

def field(row: int, col: int, text: str) -> tk.StringVar:
    
    # Label
    label = tk.Label(window, text=text)
    label.grid(row=row, column=col, padx=8, pady=8)

    # get data
    data = tk.StringVar()
    
    # Field Name
    field = tk.Entry(window, textvariable=data)
    field.config(justify='left', state='normal')
    field.grid(row=row, column=col+1, sticky='w')
    
    return data

name = field(row=1, col=0, text='Nombre')
surname = field(row=2, col=0, text='Apellidos')

def big_field(row: int, col: int, text: str):
            
    # Label
    label = tk.Label(window, text=text)
    label.grid(row=row, column=col, sticky='n', padx=8, pady=8)
    
    # Text
    field = tk.Text(window, )
    field.config(width=30, height=5, padx=4, pady=4)
    field.grid(row=row, column=col+1)
    
    return field
    
description = big_field(row=3, col=0, text='Descripción')

separator = tk.Label(window)
separator.grid(row=4)

result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.grid(row=6, column=1, sticky='w')

def set_result():
    _name = name.get()
    _surname = surname.get()
    _description = description.get("1.0", "end-1c")
    result.set(f'Resutlado: \n{_name}\n{_surname}\n{_description}')

button = tk.Button(window, text='Enviar', command=set_result)
button.config(padx=8, pady=8, bg='green', fg='white')
button.grid(row=5, column=1, sticky='w')


window.mainloop()