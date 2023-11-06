### User actions ###
from constants import strings
from .action_notes import NoteActions
from models.user import User


class UserActions:
    
    def register(self):
        print(strings.ANSWER_REG)
        username = input(strings.QUESTION_USERNAME)
        surname = input(strings.QUESTION_SURNAME)
        email = input(strings.QUESTION_EMAIL)
        password = input(strings.QUESTION_PASS)
        
        new_user = User(username, surname, email, password)
        register = new_user.register()
        
        if register[0] > 0:
            print(strings.ANSWER_REG_SUCCESS % (register[1].username, register[1].email))
        else:
            print(strings.ANSWER_REG_FAIL)
                    
    def login(self):
        print(strings.ANSWER_LOGIN)
        email = input(strings.QUESTION_EMAIL)
        password = input(strings.QUESTION_PASS)
        
        user = User('', '', email, password)
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
        
        notes = NoteActions()
        
        if action == action_list[0]:
            print(strings.GO_TO % (action_list[0]))
            notes.create(user)
            self._next_actions(user)
            
        if action == action_list[1]:
            print(strings.GO_TO % (action_list[1]))
            notes.get_all(user)
            self._next_actions(user)
            
        if action == action_list[2]:
            print(strings.GO_TO % (action_list[2]))
            notes.delete_note(user)
            self._next_actions(user)
            
        if action == action_list[3]:
            print(strings.EXIT_TEXT % (user[1]))
            exit()
            
        if action not in action_list:
            print('Elige una acción correcta')
            self._next_actions(user)
            
        