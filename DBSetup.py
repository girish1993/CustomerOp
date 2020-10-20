import sqlite3

connection = sqlite3.connect('app.db')

with open('./evolutions/schema.sql') as f:
    connection.executescript(f.read())

connection.close()
