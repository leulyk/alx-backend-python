import mysql.connector
import csv

def connect_db():
    return mysql.connector .connect(
        user='root',
        password='password',
        host='127.0.0.1'
    )

def create_database(connection):
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE {}".format("ALX_prodev"))

def connect_to_prodev():
    return mysql.connector .connect(
        user='root',
        password='password',
        host='127.0.0.1',
        database='ALX_prodev'
    )

def create_table(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """
                CREATE TABLE user_data (
                    user_id CHAR(36) PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    age DECIMAL NOT NULL
                )
            """
        )

def insert_data(connection, data):
    with connection.cursor() as cursor:
        sql = "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)"

        with open(data, 'r') as file:
            csv_data = csv.reader(file)
            next(csv_data) # skip header

            for row in csv_data:
                cursor.execute(sql, row)

            connection.commit()
