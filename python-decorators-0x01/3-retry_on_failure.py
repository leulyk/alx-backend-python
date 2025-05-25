import time
import sqlite3 
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        results = func(conn, *args, **kwargs)
        conn.close()
        return results

    return wrapper

def retry_on_failure(retries, delay):
    def retry_on_failure(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for retry_count in range(retries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    if retry_count == retries:
                        raise e
                    time.sleep(delay)
        return wrapper
    return retry_on_failure

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)
