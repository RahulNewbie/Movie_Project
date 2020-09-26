import sqlite3
import logging
from sqlite3 import Error
from utility.constants import DB_FILE


class Database:
    def __init__(self):
        self.path = DB_FILE

    def _connect_DB(self):
        """
        Connect the Database
        """
        conn = None
        try:
            conn = sqlite3.connect(self.path)
        except Error as err:
            logging.error("Error occurred while connecting database {}".format(
                str(err))
            )
        return conn

    def _close_connection(self, connection):
        """
        CLose the database connection
        """
        connection.commit()
        connection.close()

    def create_table(self):
        """
        Create movie table to store the movie data
        """
        conn = self._connect_DB()
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS movie_table (movie_title, people);"
        )
        self._close_connection(conn)

    def delete_data(self):
        """
        Delete the movie data from the table
        """
        conn = self._connect_DB()
        cur = conn.cursor()
        cur.execute("DELETE FROM movie_table;")
        self._close_connection(conn)

    def insert_movie_data(self, movie_people_dict):
        """
        Insert the moview data into database table
        """
        conn = self._connect_DB()
        cur = conn.cursor()
        cur.executemany(
            'INSERT INTO movie_table VALUES(?,?);',
            movie_people_dict.items()
        )
        self._close_connection(conn)

    def get_movie_data(self):
        """
        Fetch the stored movie data from database
        """
        conn = self._connect_DB()
        cur = conn.cursor()
        cur.execute("SELECT * FROM movie_table")
        rows = cur.fetchall()
        return rows
