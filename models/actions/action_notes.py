### Note Actions ###

from models.note import Note
from constants.strings import QUESTION_NOTE_CREATE, QUESTION_NOTE_TITLE, QUESTION_NOTE_DESCRIPTION, ANSWER_NOTE_CREATE_SUCCESS, ANSWER_NOTE_CREATED_FAIL, ANSWER_NOTE_GETTING


class NoteActions:
    
    def create(self, user):
        print(QUESTION_NOTE_CREATE % (user[1]))
        
        title = input(QUESTION_NOTE_TITLE)
        description = input(QUESTION_NOTE_DESCRIPTION)
        
        note = Note(user[0], title, description)
        result = note.create()
        
        if result[0] == 0:
            print(ANSWER_NOTE_CREATED_FAIL)
        else:
            print(ANSWER_NOTE_CREATE_SUCCESS % (note.title))
        
    def get(self, user):
        print(ANSWER_NOTE_GETTING % (user[1]))
        
        note = Note(user[0], '', '')
        result = note.get_notes()
        
        for note in result:
            print(note)
