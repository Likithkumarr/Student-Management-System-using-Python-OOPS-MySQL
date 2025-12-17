show databases;
create database student_db;
use student_db;

create table students
(
roll_no INT PRIMARY KEY,
name VARCHAR(100),
age INT,
course VARCHAR(50),
marks FLOAT
);

select * from students;

#1.Display All Students
select * from students;

#2.Find Student with Highest Marks
SELECT name, marks
FROM students
ORDER BY marks DESC
LIMIT 1;

#3.Find Students Scoring Above 75
SELECT name, course, marks
FROM students
WHERE marks > 75;

#4.Count Total Students
SELECT COUNT(*) AS total_students
FROM students;

#5.Find Average Marks
SELECT AVG(marks) AS average_marks
FROM students;

#6.List Students Enrolled in Java Course
SELECT name, age, marks
FROM students
WHERE course = 'Java';

#7.Find Students Aged 21 or Above
SELECT name, age
FROM students
WHERE age >= 21;

#8.Course-wise Student Count
SELECT course, COUNT(*) AS student_count
FROM students
GROUP BY course;

#9.Find Students with Lowest Marks
SELECT name, marks
FROM students
ORDER BY marks ASC
LIMIT 1;

#10.Sort Students by Marks (Descending)
SELECT name, course, marks
FROM students
ORDER BY marks DESC;

#11.Students Between Age 18 and 22
SELECT name, age
FROM students
WHERE age BETWEEN 18 AND 22;

#13.Courses with Average Marks Above 75
SELECT course, AVG(marks) AS avg_marks
FROM students
GROUP BY course
HAVING avg_marks > 75;
