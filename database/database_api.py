import sqlite3
from sqlite3 import Error
from utility.constants import DB_FILE


class Database:
    def __init__(self):
        self.path = DB_FILE

    def _connect_DB(self):
        conn = None
        try:
            conn = sqlite3.connect(self.path)
        except Error as err:
            print("Error occurred while connecting database {}".format(str(err)))
        return conn

    def _close_connection(self, connection):
        connection.commit()
        connection.close()

    def create_table(self):
        conn = self._connect_DB()
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS movie_table (movie_title, people);")
        self._close_connection(conn)

    def delete_data(self):
        conn = self._connect_DB()
        cur = conn.cursor()
        cur.execute("DELETE FROM movie_table;")
        self._close_connection(conn)

    def insert_movie_data(self, movie_people_dict):
        conn = self._connect_DB()
        cur = conn.cursor()
        cur.executemany(
            'INSERT INTO movie_table VALUES(?,?);',
            movie_people_dict.items()
        )
        self._close_connection(conn)

    def get_movie_data(self):
        conn = self._connect_DB()
        cur = conn.cursor()
        cur.execute("SELECT * FROM movie_table")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print(type(rows))
        return rows
