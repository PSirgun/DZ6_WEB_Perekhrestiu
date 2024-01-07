SELECT students.name_stud AS name_student, students.group_name AS group_name, courses.name_course AS name_course, grade 
from grades
join students ON grades.id_stud = students.id_stud 
join groups ON students.group_name = groups.g_name
join courses ON grades.id_course = courses.id_course 
WHERE groups.g_name = COALESCE (?, 'group01') AND courses.name_course = COALESCE (?, 'Physic')