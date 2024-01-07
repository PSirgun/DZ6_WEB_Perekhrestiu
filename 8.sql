SELECT teachers.name_teach AS teacher_name, AVG(grade) AS avg_grade
FROM grades
JOIN courses ON grades.id_course = courses.id_course 
JOIN teachers ON courses.id_teach = teachers.id_teach 
WHERE teachers.id_teach = COALESCE (?, teachers.id_teach)
GROUP BY teachers.id_teach 