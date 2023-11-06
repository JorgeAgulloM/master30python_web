### Operations ###

def operation(operation: int, value_one: str, value_two: str) -> float | str:
    switcher = {
        0: _sum,
        1: _extract,
        2: _product,
        3: _divide
    }
    
    calculate = switcher.get(operation, lambda: 'Error')
    return calculate(value_one, value_two)

############################ Private Funtions ############################

def _sum(value_one: str, value_two: str) -> float | str:
    result = _validate(value_one, value_two)
    if type(result) is str:
        return result
    return result[0] + result[1]       

def _extract(value_one: str, value_two: str) -> float | str:
    result = _validate(value_one, value_two)
    if type(result) is str:
        return result
    return result[0] - result[1] 

def _product(value_one: str, value_two: str) -> float | str:
    result = _validate(value_one, value_two)
    if type(result) is str:
        return result
    return result[0] * result[1] 

def _divide(value_one: str, value_two: str) -> float | str:
    result = _validate(value_one, value_two)
    if type(result) is str:
        return result
    return result[0] / result[1]

def _validate(value_one: str, value_two: str) -> tuple | str:
    float_one = _parse_float(value_one)
    float_two = _parse_float(value_two)
    
    if type(float_one) is not float:
        return float_one
    if type(float_two) is not float:
        return float_two
    return float_one, float_two
        
def _parse_float(value: str) -> float | str:
    try: 
        return float(value)
    except Exception as e:
        return f'Debes introducir números. Error : {e}'
    