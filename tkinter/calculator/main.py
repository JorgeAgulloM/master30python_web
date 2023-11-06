### Calulator ###
from objects import  mainloop, field, button_operator, msg_error, msg_box, separator, result_list
from operations import operation as op
from data import value_one, value_two, results

def calculate(operation: int):
    result = op(operation, value_one.get(), value_two.get())
    
    if type(result) is str:
        msg_error(result)
    else:
        value_one.set('')
        value_two.set('')
        results.append(f'Resutado: {result}')

        result_list(results)
        msg_box(results)

value_one = field(text='Primer valor')
value_two = field(text='Segundo valor')

separator()

button_operator(signal='+', operation=lambda:calculate(0))
button_operator(signal='-', operation=lambda:calculate(1))
button_operator(signal='x', operation=lambda:calculate(2))
button_operator(signal='/', operation=lambda:calculate(3))

result_list(results)

mainloop()
