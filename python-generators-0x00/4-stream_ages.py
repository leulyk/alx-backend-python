
seed = __import__('seed')

def stream_user_ages():
    with seed.connect_to_prodev() as connection:
        with connection.cursor(buffered=True, dictionary=True) as cursor:
            query = "SELECT * FROM user_data"
            cursor.execute(query)
            for record in cursor:
                yield record['age']

def calculate_average_age():
    count = total = 0
    for age in stream_user_ages():
        total += age
        count += 1

    average_age = total / count if count else 0
    print(f"Average age of users: {average_age:.2f}")
