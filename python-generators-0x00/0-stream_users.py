import mysql.connector

seed = __import__('seed')

def stream_users():
    with seed.connect_to_prodev() as connection:
        with connection.cursor(buffered=True, dictionary=True) as cursor:
            query = "SELECT * FROM user_data"
            cursor.execute(query)
            for record in cursor:
                yield record
