### User actions ###
from constants import strings
import models.user.user as user_model
import actions.note as notes

class Actions:
    
    def register(self):
        print(strings.ANSWER_REG)
        username = input(strings.QUESTION_USERNAME)
        surname = input(strings.QUESTION_SURNAME)
        email = input(strings.QUESTION_EMAIL)
        password = input(strings.QUESTION_PASS)
        
        new_user = user_model.User(username, surname, email, password)
        register = new_user.register()
        
        if register[0] > 0:
            print(strings.ANSWER_REG_SUCCESS % (register[1].username, register[1].email))
        else:
            print(strings.ANSWER_REG_FAIL)
                    
    def login(self):
        print(strings.ANSWER_LOGIN)
        email = input(strings.QUESTION_EMAIL)
        password = input(strings.QUESTION_PASS)
        
        user = user_model.User('', '', email, password)
        user = user.login()
        
        if len(user) == 0:
            print(strings.ANSWER_LOGIN_FAIL)
        else:
            username = user[1]
            print(strings.ANSWER_LOGIN_SUCCESS % (username))
            self._next_actions(user)
            
    def _next_actions(self, user):
        print(strings.QUESTION_ACCTIONS_TODO)
        
        action = input(strings.QUESTION_WANT_TODO % (user[1]))
        
        action_list = [
            strings.CREATE,
            strings.NOTE,
            strings.DELETE,
            strings.EXIT,
        ]
        
        if action == action_list[0]:
            print(strings.GO_TO % (action_list[0]))
            note = notes.Actions()
            note.create(user)
            self._next_actions(user)
            
        if action == action_list[1]:
            print(strings.GO_TO % (action_list[1]))
            self._next_actions(user)
            
        if action == action_list[2]:
            print(strings.GO_TO % (action_list[2]))
            self._next_actions(user)
            
        if action == action_list[3]:
            print(strings.EXIT_TEXT % (user[1]))
            exit()
            
        if action not in action_list:
            print('Elige una acción correcta')
            self._next_actions(user)
            
        