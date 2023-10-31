### Query Constants ###

INSERT_REG = 'INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)'
SELECT_LOGIN = 'SELECT * FROM users WHERE email = %s AND pass_wd = %s'