"""
Proyecto Python y MySql:
- Iniciar Asistente
- Login o registro
- Crear usuario
- Identificar usuario
- Crear, mostrar y borrar notas
"""

from constants import strings
from models.actions.action_users import UserActions as actions

make = actions()

print(f"""
    Acciones disponibles:
    - {strings.REGISTRO}
    - {strings.LOGIN}      
""")

accion = input("¿Que quieres hacer?")

if accion == strings.REGISTRO:
    make.register()
        
if accion == strings.LOGIN:
    make.login()