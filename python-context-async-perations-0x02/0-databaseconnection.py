import sqlite3

class DatabaseConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        return (self.connection, self.cursor)

    def __exit__(self, type, value, traceback):
        self.connection.close()

with DatabaseConnection('users.db') as (connection, cursor):
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(users)
