SELECT students.name_stud AS student_name, AVG(grades.grade) AS avg_grade
FROM grades
JOIN students ON grades.id_stud = students.id_stud
GROUP BY students.id_stud
ORDER BY avg_grade DESC
LIMIT 5;
