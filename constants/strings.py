### Constants Strings ###

REGISTRO: str = 'registro'
LOGIN: str = 'login'
CREATE: str = 'crear'
NOTE: str = 'mostrar'
DELETE: str = 'eliminar'
EXIT: str = 'salir'

TO_DO: str = '\n¿Que quieres hacer? '
GO_TO: str = '\nVamos a %s'
EXIT_TEXT: str = '\nHasta luego %s!'

ANSWER_REG: str = '\nOK!! Vamos a registrarte en el sistema...'
ANSWER_REG_SUCCESS: str = '\n!Perfecto %s te has registrado con el email %s!'
ANSWER_REG_FAIL: str = '\nNo se ha completado el registro correctamente.'

ANSWER_LOGIN: str = '\nVale!! Identificate por favor...'
ANSWER_LOGIN_SUCCESS: str = '\n¡Bienvenido %s! estás logeado.'
ANSWER_LOGIN_FAIL: str = '\nError en usuario o contraseña'

QUESTION_USERNAME: str = '\nIntroduce tu nombre: '
QUESTION_SURNAME: str = '\nahora tus apellidos: '
QUESTION_EMAIL: str = '\nIntroduce un e-mail: '
QUESTION_PASS: str = '\ny tu contraseña: '

QUESTION_WANT_TODO: str = '\n¿Que quieres hacer %s?: '
QUESTION_ACCTIONS_TODO: str = f"""\n
    Acciones disponibles:
    - Crear nota ({CREATE})
    - Mostrar notas ({NOTE})
    - Eliminar nota ({DELETE})
    - Salir ({EXIT})
"""

QUESTION_NOTE_CREATE: str = '\nPerfecto. %s, vamos a crear una nota...'
QUESTION_NOTE_TITLE: str = '\nIntroduce el título de la nota: '
QUESTION_NOTE_DESCRIPTION: str = '\nIntroduce la descripción de la nota: '

ANSWER_NOTE_CREATE_SUCCESS: str = '\nTu nota %s has sido guardada con éxito'
ANSWER_NOTE_CREATED_FAIL: str = '\nError al guardar la nota.'
