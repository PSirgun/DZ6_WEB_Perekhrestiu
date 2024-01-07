SELECT students.name_stud, courses.name_course, teachers.name_teach
FROM students
JOIN grades ON students.id_stud = grades.id_stud
JOIN courses ON grades.id_course = courses.id_course
JOIN teachers ON courses.id_teach = teachers.id_teach
WHERE students.id_stud = COALESCE (?, students.id_stud) AND teachers.id_teach = COALESCE (?, teachers.id_teach)
GROUP BY courses.name_course 
