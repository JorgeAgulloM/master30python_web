#### Objects Tkinter ####

from tkinter import Tk, Label, StringVar, Button, Entry, Text, Frame, messagebox as mbox, NORMAL, DISABLED, END

window = Tk()
window.title('Calculadora con Tkinter y Python')

def mainloop() -> ():
    return window.mainloop()

def frame() -> Frame:
    frame = Frame(window, width=250, height=150)
    frame.config(
        bd=5,
        relief='solid'
    )
    frame.pack(side='top', anchor='center', padx=8, pady=8)
    frame.pack_propagate(False)
    return frame

my_frame = frame()

text = Text(window)
text.config(width=30)
text.pack()
    
def field(text: str) -> StringVar:
    data = StringVar()
    
    Label(my_frame, text=text).pack()
    Entry(my_frame, textvariable=data).pack()
    
    return data

def button_operator(signal: str, operation):
    Button(my_frame, text=signal, command=operation).pack(side='left', padx=4, fill='x', expand=True)

def msg_error(error: str):
    mbox.showerror('Error', f'Error: {error}')

def msg_box(result: float):
    mbox.showinfo('Operación', f'Resutado: {result}')

def separator():
    Label(my_frame, text='').pack()
    
def result_list(results):
    content = '\n'.join(results)
    text.config(state=NORMAL)
    text.delete(1.0, END)
    text.insert(END, content)
    text.config(state=DISABLED)
    