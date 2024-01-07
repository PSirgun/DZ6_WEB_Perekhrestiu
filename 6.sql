SELECT name_stud, group_name 
FROM students s 
WHERE group_name = COALESCE (?, 'group01')