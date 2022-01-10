import sqlite3

def sql_createTables():
    filename = '../database/data.db'
    commands = [
        "CREATE TABLE Posts (id INTEGER PRIMARY KEY, timestamp TIMESTAMP NOT NULL, user VARCHAR(100), description TEXT, path TEXT NOT NULL, side TEXT NOT NULL, timeframe TEXT NOT NULL, votes INTEGER NOT NULL)",
    ]
    try:
        conn = sqlite3.connect(filename)
        c = conn.cursor()
        for i in commands:
            c.execute(i)
    except Exception as e:
        print(e)


sql_createTables()