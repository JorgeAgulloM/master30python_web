### Query Constants ###

# User
INSERT_USER = 'INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)'
SELECT_LOGIN = 'SELECT * FROM users WHERE email = %s AND pass_wd = %s'

# Note
INSERT_NOTE = 'INSERT INTO notes VALUES(null, %s, %s, %s, NOW())'
SELECT_NOTES = 'SELECT * FROM notes WHERE user_id = %s'
DELETE_NOTE = "DELETE FROM notes WHERE user_id = %s AND title LIKE '%s'"
