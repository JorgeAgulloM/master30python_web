### DB control acctions ###

import mysql.connector as conn

database = conn.connect(
    host='localhost',
    user='root', 
    passwd='',
    database='master_python',
    port=3306
)

cursor = database.cursor(buffered=True)

class DBControl():
    
    def insert(self, query, data):
        try:
            cursor.execute(query, data)
            database.commit()
        except:
            return 0
        
        return cursor.rowcount
    
    def select(self, query, data):
        try:
            cursor.execute(query, data)
        except:
            return []
        
        return cursor.fetchone()
        