### User actions ###
from constants import strings
import models.user.user as model

class Actions:
    
    def register(self):
        print(strings.ANSWER_REG)
        username = input(strings.QUESTION_USERNAME)
        surname = input(strings.QUESTION_SURNAME)
        email = input(strings.QUESTION_EMAIL)
        password = input(strings.QUESTION_PASS)
        
        new_user = model.User(username, surname, email, password)
        register = new_user.register()
        
        if register[0] > 0:
            print(strings.ANSWER_REG_SUCCESS % (register[1].username, register[1].email))
        else:
            print(strings.ANSWER_REG_FAIL)
                    
    def login(self):
        print(strings.ANSWER_LOGIN)
        email = input(strings.QUESTION_EMAIL)
        password = input(strings.QUESTION_PASS)
        
        user = model.User('', '', email, password)
        login = user.login()
        
        if len(login) == 0:
            print(strings.ANSWER_LOGIN_FAIL)
        else:
            print(strings.ANSWER_LOGIN_SUCCESS % (login[1]))