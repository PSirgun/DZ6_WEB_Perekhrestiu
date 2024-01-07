SELECT students.name_stud AS student_name, courses.name_course as name_course, AVG(grades.grade) AS avg_grade
FROM grades
JOIN students ON grades.id_stud = students.id_stud 
JOIN courses ON grades.id_course = courses.id_course 
WHERE name_course = COALESCE(?, 'Physic')
GROUP BY grades.id_stud
ORDER BY avg_grade DESC 
LIMIT 1
