### User Model ###

import datetime as dt
import hashlib as hash
from db.control import DBControl
from constants.querys import INSERT_USER, SELECT_LOGIN

db_control = DBControl()

class User():
    
    def __init__(self, username, surname, email, password):
        self.username=username
        self.surname=surname
        self.email=email
        self.password=password
        
    def register(self):
        date = dt.datetime.now()
        encryp = self._encrypt()
        
        query = INSERT_USER
        user = (self.username, self.surname, self.email, encryp.hexdigest(), date)
        
        return [db_control.insert(query, user), self]
        
    def login(self):
        query = SELECT_LOGIN
        encryp = self._encrypt()
        
        user = (self.email, encryp.hexdigest())

        return db_control.select(query, user)
    
    def _encrypt(self):
        encryp = hash.sha256()
        encryp.update(self.password.encode('utf8'))
        return encryp