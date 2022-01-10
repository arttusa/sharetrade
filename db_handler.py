import sqlite3
import datetime
# get_post()
# add_post()





def add_post():
    filename = "../database/data.db"
    post = {
        "timestamp": datetime.datetime.now(),
        "user": "user123",
        "description": "Surfing the 10-day. Getting ready to break out.",
        "path": "./imgs/000",
        "side": "Long",
        "timeframe": "1d",
        "votes": 0,
    }
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    try:
        c.execute("BEGIN TRANSACTION")
        c.executemany(f'INSERT INTO Posts({post.timestamp} {post.user} {post.description} {post.path} {post.side} {post.timeframe} {post.votes})')
        c.execute("COMMIT TRANSACTION")
    except Exception as e:
        print("SQL Error", e)