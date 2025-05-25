import sqlite3
import time
import functools

query_cache = {}

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        results = func(conn, *args, **kwargs)
        conn.close()
        return results
    return wrapper

def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query):
        if query in query_cache:
            return query_cache[query]

        result = func(conn, query)
        query_cache[query] = result

        return result
    
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will cache the result
start_time = time.time()
users = fetch_users_with_cache(query="SELECT * FROM users")
time_without_cache = time.time() - start_time

# Second call will use the cached result
start_time = time.time()
users_again = fetch_users_with_cache(query="SELECT * FROM users")
time_after_cache = time.time() - start_time

print("Before cache: {}\nAfter cache: {}".format(time_without_cache, time_after_cache))
