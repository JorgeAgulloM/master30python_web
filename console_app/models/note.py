### Note model ###
from db.db_control import DBControl
from constants.querys import INSERT_NOTE, SELECT_NOTES, DELETE_NOTE

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
    
    def get_notes(self):
        query = SELECT_NOTES % (self.user_id)
        
        return db_control.select(query, None)
    
    def delete(self):
        query = DELETE_NOTE % (self.user_id ,f"%{self.title}%")
        print(query)
        return [db_control.delete_one(query, None), self]
    