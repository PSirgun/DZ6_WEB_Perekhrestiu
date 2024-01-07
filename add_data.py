"""

Наповнюю таблиці

"""
import sqlite3
from contextlib import contextmanager
from faker import Faker
import random
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

fake = Faker()
ALL_GRADES = ['5','4','3','2','1','0'] 

@contextmanager
def main(num_studs=50, num_teachers=3):
    connection = sqlite3.connect('DB_dz6.db')

    cursor = connection.cursor()

 #-----------------------------------------------------------------------------------------------------------------------------   
    group_ins = [('group01',), ('group02',), ('group03',)]
    cursor.executemany('INSERT OR IGNORE INTO groups (g_name) VALUES(?)', group_ins)   
    
 #-----------------------------------------------------------------------------------------------------------------------------   
    for _ in range(num_studs):
            student_name = fake.name()
            random_group = random.choice(group_ins)[0]
            cursor.execute('INSERT INTO students (name_stud, group_name) VALUES (?, ?)', (student_name, random_group))
    
        
 
 #-----------------------------------------------------------------------------------------------------------------------------   
    teachers_list = []
    for _ in range (num_teachers):
        teacher_degree = random.choice(['Professor', 'Doctor'])
        teacher_name = (f'{teacher_degree} {fake.last_name()}',)
        teachers_list.append(teacher_name)
    print (teachers_list)
        
    courses_list = [('Math',), ('Physic',), ('Music',), ('Sport',), ('History',)]
    num_courses = len(courses_list)

    random_teach_id = [random.randint(1, num_teachers) for _ in range(num_courses)]
    combined_courses = [(course[0], teacher_id) for course, teacher_id in zip(courses_list, random_teach_id)]    
    
    cursor.executemany ('INSERT INTO teachers (name_teach) VALUES(?)', teachers_list)
    cursor.executemany('INSERT INTO courses (name_course, id_teach) VALUES(?, ?)', combined_courses)

 #-----------------------------------------------------------------------------------------------------------------------------   
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)

    

    grades_list = []
    for stud_id in range(1, num_studs+1):
        for course_id in range(1, num_courses+1):
            grade = random.choice(ALL_GRADES)
            num_grades = random.randint(1, 5)
            for _ in range(num_grades):
                random_date = fake.date_between(start_date=start_date, end_date=end_date)
                grades_list.append((stud_id, course_id, grade, random_date))
    cursor.executemany('INSERT INTO grades (id_stud, id_course, grade, date_received) VALUES(?, ?, ?, ?)', grades_list)
    
    yield

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    with main():
        print('all ok')