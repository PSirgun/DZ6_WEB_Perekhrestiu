import sqlite3
from contextlib import contextmanager

database = './DB_dz6.db'


@contextmanager
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        yield conn
        conn.commit()
        conn.close()
    except IndexError:
        print (Exception)
        conn.rollback()
        conn.close()