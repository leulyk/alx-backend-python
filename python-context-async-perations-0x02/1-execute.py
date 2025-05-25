import sqlite3

class ExecuteQuery:
    def __init__(self, query, conn=None, params=[]):
        self.query = query
        self.params = params
        self.connection = conn
        self.cursor = None
    
    def __enter__(self):
        """ works only for select queries """
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()
    
    def __exit__(self, type, value, traceback):
        if self.connection:
            if not type:
                self.connection.commit()
            else:
                self.connection.rollback()

class DatabaseConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        return self.connection

    def __exit__(self, type, value, traceback):
        self.connection.close()

# tests

db_file = "users.db"

with DatabaseConnection(db_file) as conn:
    query1 = "SELECT * from users"
    query2 = "SELECT * from users where id > ?"
    params = [2]

    with ExecuteQuery(query1, conn) as result:
        print(result)

    with ExecuteQuery(query2, conn, params) as result:
        print(result)
