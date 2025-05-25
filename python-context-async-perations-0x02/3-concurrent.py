import asyncio
import aiosqlite

async def async_fetch_users():
    async with aiosqlite.connect('users.db') as db:
        async with db.execute("SELECT * FROM users") as cursor:
            results = await cursor.fetchall()
        
    return results
        

async def async_fetch_older_users():
    async with aiosqlite.connect('users.db') as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            results = await cursor.fetchall()
            
    return results

async def fetch_concurrently():
    all_users, old_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

    if all_users:
        for index, user in enumerate(all_users):
            print(f"{index}: {user}")

    if old_users:
        for index, user in enumerate(old_users):
            print(f"{index}: {user}")

asyncio.run(fetch_concurrently())
