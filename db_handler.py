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



def get_posts():
    # Get posts from database
    return 