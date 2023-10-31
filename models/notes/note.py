### Note model ###
from db.control import DBControl
from constants.querys import INSERT_NOTE

db_control = DBControl()

class Note():
    
    def __init__(self, user_id, title, description):
        self.user_id = user_id
        self.title = title
        self.description = description
        
    def create(self):
        query = INSERT_NOTE
        note = (self.user_id, self.title, self.description)
                
        return [db_control.insert(query, note), self]
    
    