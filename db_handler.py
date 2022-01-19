from importlib.resources import path
import sqlite3

DATABASE = "./database/data.db"

def add_post(user, description, path):
    post = {
        "user": user,
        "description": description,
        "path": path,
        "votes": 0
    }

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    try:
        c.execute("BEGIN TRANSACTION")
        c.execute("INSERT INTO Posts (user, description, path, votes) VALUES (?, ?, ?, ?)", (post["user"], post["description"], post["path"], post["votes"]))
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
            "path": result[4],
            "votes": result[5]
        }
        posts.append(post)
    return posts