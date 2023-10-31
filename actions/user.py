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
            username = login[1]
            print(strings.ANSWER_LOGIN_SUCCESS % (username))
            self._next_actions(username)
            
    def _next_actions(self, username):
        print(strings.QUESTION_ACCTIONS_TODO)
        
        action = input(strings.QUESTION_WANT_TODO % (username))
        
        action_list = [
            strings.CREATE,
            strings.NOTE,
            strings.DELETE,
            strings.EXIT,
        ]
        
        if action == action_list[0]:
            print(strings.GO_TO % (action_list[0]))
            self._next_actions(username)
            
        if action == action_list[1]:
            print(strings.GO_TO % (action_list[1]))
            self._next_actions(username)
            
        if action == action_list[2]:
            print(strings.GO_TO % (action_list[2]))
            self._next_actions(username)
            
        if action == action_list[3]:
            print(strings.EXIT_TEXT % (username))
            exit()
            
        if action not in action_list:
            print('Elige una acción correcta')
            self._next_actions(username)
            
        