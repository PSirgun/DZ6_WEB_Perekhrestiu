SELECT students.name_stud, students.id_stud, courses.name_course
FROM students
JOIN grades ON students.id_stud = grades.id_stud
JOIN courses ON grades.id_course = courses.id_course
WHERE students.id_stud  = COALESCE(?, students.id_stud)
GROUP BY courses.name_course 
