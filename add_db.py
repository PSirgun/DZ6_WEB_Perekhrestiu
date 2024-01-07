"""

Створюю базу даних та таблиці.

"""

import sqlite3
from contextlib import contextmanager
import time

@contextmanager
def main():
    connection = sqlite3.connect('DB_dz6.db')

    cursor = connection.cursor()

    print(type(cursor))

    cursor.execute('DROP TABLE IF EXISTS groups')
    cursor.execute('''CREATE TABLE IF NOT EXISTS groups (g_name VARCHAR(7) PRIMARY KEY)''')

    cursor.execute('DROP TABLE IF EXISTS students')
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id_stud INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name_stud VARCHAR(30),
                    group_name VARCHAR(7),
                    FOREIGN KEY (group_name) REFERENCES groups (g_name)
                    )''')


    cursor.execute('DROP TABLE IF EXISTS teachers')
    cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (id_teach INTEGER PRIMARY KEY AUTOINCREMENT, name_teach VARCHAR(30))''')


    cursor.execute('DROP TABLE IF EXISTS courses')
    cursor.execute('''CREATE TABLE IF NOT EXISTS courses (id_course INTEGER PRIMARY KEY AUTOINCREMENT, name_course VARCHAR(15),
                    id_teach VARCHAR(30),
                    FOREIGN KEY (id_teach) REFERENCES teachers (id_teach) )''')


    cursor.execute('DROP TABLE IF EXISTS grades')
    cursor.execute('''CREATE TABLE IF NOT EXISTS grades (id_stud INTEGER,
                    id_course INTEGER,
                    grade INTEGER,
                    date_received DATE,
                    FOREIGN KEY (id_course) REFERENCES courses (id_course),
                    FOREIGN KEY (id_stud) REFERENCES students (id_stud)
                    )''')

    yield

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
   with main() as mf:
       print('allok')
