import sqlite3

class ExecuteQuery:
    def __init__(self, db_file, query, params=[]):
        self.db_file = db_file
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)

        # works only for select queries
        return self.cursor.fetchall()
    
    def __exit__(self, type, value, traceback):
        if self.connection:
            if not type:
                self.connection.commit()
            else:
                self.connection.rollback()

# tests

db_file = "users.db"
query1 = "SELECT * from users"
query2 = "SELECT * from users where id > ?"
params = [2]

with ExecuteQuery(db_file, query1) as result:
    print(result)

with ExecuteQuery(db_file, query2, params) as result:
    print(result)
