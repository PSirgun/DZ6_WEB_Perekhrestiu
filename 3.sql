SELECT groups.g_name, courses.name_course, AVG(grades.grade) AS average_grade
FROM groups
JOIN students ON groups.g_name = students.group_name
JOIN grades ON students.id_stud = grades.id_stud
JOIN courses ON grades.id_course = courses.id_course
WHERE courses.name_course = COALESCE(?, 'Physic')
GROUP BY groups.g_name;
