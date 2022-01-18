from importlib.resources import path
import re
import sqlite3
import datetime
# get_post()
# add_post()

DATABASE = "./database/data.db"

def add_post(user, description, path):
    post = {
        "user": user,
        "description": description,
        "path": path
    }

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    try:
        c.execute("BEGIN TRANSACTION")
        c.execute("INSERT INTO Posts (user, description, path) VALUES (?, ?, ?)", (post["user"], post["description"], post["path"]))
        c.execute("COMMIT TRANSACTION")
    except Exception as e:
        print("SQL Error", e)


# Fetches ten recent posts
def get_posts():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM Posts ORDER BY id DESC LIMIT 10')
    results = c.fetchall()
    posts = []
    for result in results:
        post = {
            "timestamp": result[1],
            "user": result[2],
            "description": result[3],
            "path": result[4]
        }
        posts.append(post)
    return posts