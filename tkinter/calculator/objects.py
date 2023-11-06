#### Objects Tkinter ####

from tkinter import Tk, Label, StringVar, Button, Entry, Frame, messagebox as mbox

def frame(window: Tk) -> Frame:
    frame = Frame(window, width=250, height=150)
    frame.config(
        bd=5,
        relief='solid'
    )
    frame.pack(side='top', anchor='center', padx=8, pady=8)
    frame.pack_propagate(False)
    return frame

def field(frame: Frame ,text: str) -> StringVar:
    data = StringVar()
    
    Label(frame, text=text).pack()
    Entry(frame, textvariable=data).pack()
    
    return data

def button_operator(frame: Frame, signal: str, operation):
    Button(frame, text=signal, command=operation).pack(side='left', padx=4, fill='x', expand=True)

def msg_error(error: str):
    mbox.showerror('Error', f'Error: {error}')

def msg_box(result: float):
    mbox.showinfo('Operación', f'Resutado: {result}')

def separator(frame: Frame):
    Label(frame, text='').pack()