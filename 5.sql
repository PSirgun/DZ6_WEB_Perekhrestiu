SELECT teachers.name_teach AS name_teacher, courses.name_course
FROM courses
JOIN teachers ON courses.id_teach = teachers.id_teach
WHERE teachers.id_teach = COALESCE(?, '2')