### Note Actions ###

from models.note import Note
from constants.strings import ANSWER_NOTE_CREATE, QUESTION_NOTE_TITLE, QUESTION_NOTE_DESCRIPTION, ANSWER_NOTE_CREATE_SUCCESS, ANSWER_NOTE_CREATED_FAIL, ANSWER_NOTE_GETTING, QUESTION_NOTE_DELETE, ANSWER_NOTE_DELETE, ANSWER_NOTE_DELETE_SUCCESS, ANSWER_NOTE_DELETE_FAIL


class NoteActions:
    
    def create(self, user):
        print(ANSWER_NOTE_CREATE % (user[1]))
        
        title = input(QUESTION_NOTE_TITLE)
        description = input(QUESTION_NOTE_DESCRIPTION)
        
        note = Note(user[0], title, description)
        result = note.create()
        
        if result[0] == 0:
            print(ANSWER_NOTE_CREATED_FAIL)
        else:
            print(ANSWER_NOTE_CREATE_SUCCESS % (note.title))
        
    def get_all(self, user):
        print(ANSWER_NOTE_GETTING % (user[1]))
        
        note = Note(user[0], '', '')
        result = note.get_notes()
        
        for note in result:
            print('\n****************************')
            print(note[2])
            print(note[3])
            print('****************************')
            
    def delete_note(self, user):
        print(ANSWER_NOTE_DELETE % (user[1]))
        
        title_note = input(QUESTION_NOTE_DELETE)
        
        note = Note(user[0], title_note, '')
        result = note.delete()
        
        if result[0] > 0:
            print(ANSWER_NOTE_DELETE_SUCCESS % (result[1].title))
        else: 
            print(ANSWER_NOTE_DELETE_FAIL % (title_note))
        
