### Calulator ###
from tkinter import Tk, Label, StringVar
from objects import frame, field, button_operator, msg_error, msg_box, separator
from operations import operation as op

window = Tk()
window.title('Calculadora con Tkinter y Python')

value_one = StringVar()
value_two = StringVar()
my_frame = frame(window)

def calculate(operation: int):
    result = op(operation, value_one.get(), value_two.get())
    
    if type(result) is str:
        msg_error(result)
    else:
        value_one.set('')
        value_two.set('')
        msg_box(result)

value_one = field(my_frame, text='Primer valor')
value_two = field(my_frame, text='Segundo valor')

separator(my_frame)

button_operator(my_frame, signal='+', operation=lambda:calculate(0))
button_operator(my_frame, signal='-', operation=lambda:calculate(1))
button_operator(my_frame, signal='x', operation=lambda:calculate(2))
button_operator(my_frame, signal='/', operation=lambda:calculate(3))

window.mainloop()
