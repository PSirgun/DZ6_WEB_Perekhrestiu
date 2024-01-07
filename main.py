from connection import create_connection, database
from pathlib import Path
import time

def sql_use(adr, param=None):
    with create_connection(database) as conn:
        with open(adr, 'r') as fh:
            sql = fh.read()
            
        cursor = conn.cursor()
        time.sleep(1)
        if param:
           cursor.execute(sql, param) 
        else:
            try:
                cursor.execute(sql, (None,))
            except Exception:
                cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            print (i)
        cursor.close()

if __name__ == '__main__':
    print ('''HElP: 
courses_list = [('Math',), ('Physic',), ('Music',), ('Sport',), ('History',)]
teachers use ID  - 1, 2, 3 
students ise ID - 1-50
group_ins = [('group01',), ('group02',), ('group03',)]
             ''')
    while True:
        user_input = input(">>>")
        
        if user_input == '.':
            break
        
        user_input = user_input.split()
        
        adr = user_input[0]+'.sql'
        
        if Path(adr).exists():
            if len(user_input) > 1:
                params = user_input[1:]
                print (params)
                sql_use(adr, params)
            else:
               sql_use(adr)
        
