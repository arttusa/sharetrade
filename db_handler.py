from importlib.resources import path
import sqlite3

DATABASE = "./database/data.db"

def add_post(user, symbol, description, path):
    post = {
        "user": user,
        "symbol": symbol,
        "description": description,
        "path": path,
        "votes": 0
    }

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    try:
        c.execute("BEGIN TRANSACTION")
        c.execute("INSERT INTO Posts (user, symbol, description, path, votes) VALUES (?, ?, ?, ?, ?)", (post["user"], post["symbol"], post["description"], post["path"], post["votes"]))
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
        splitted_arr = result[5].split("\\")
        path = splitted_arr[len(splitted_arr) - 1] # Return only the last path of the picture
        post = {
            "timestamp": result[1],
            "user": result[2],
            "symbol": result[3],
            "description": result[4],
            "path": path,
            "votes": result[6]
        }
        posts.append(post)
    return posts