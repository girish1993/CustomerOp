import sqlite3


class Connection:

    def __init__(self):
        self.database = "app.db"
        self.conn = sqlite3.connect(self.database)
        self.conn.row_factory = sqlite3.Row

    def get_db_connection(self):
        return self.conn

