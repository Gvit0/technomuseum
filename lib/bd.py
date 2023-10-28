import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS main (
    username STRING,
    password STRING,
    rights   STRING);
    """)
def reg(user, password, rights):
    datatosend = (user,password,rights)
    cursor.execute("INSERT INTO people (username, password, rights) VALUES (?,?,?)",datatosend)
create_table()