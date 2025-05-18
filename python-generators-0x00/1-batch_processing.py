
seed = __import__('seed')

def batch_processing(batch_size):
    for users in stream_users_in_batches(batch_size):
        for user in users:
            if user['age'] > 25:
                print(user)
    return

def stream_users_in_batches(batch_size):
    with seed.connect_to_prodev() as connection:
        with connection.cursor(buffered=True, dictionary=True) as cursor:
            offset = 0
            while True:
                query = "SELECT * FROM user_data LIMIT {} OFFSET {}".format(batch_size, offset)
                cursor.execute(query)
                rows = cursor.fetchall()

                if not rows:
                    break

                offset += batch_size
                yield rows
