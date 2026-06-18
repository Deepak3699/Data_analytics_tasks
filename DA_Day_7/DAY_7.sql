
CREATE DATABASE internship_sql;
USE internship_sql;
-- Create Students Table
CREATE TABLE students (
student_id INT PRIMARY KEY,
student_name VARCHAR(50),
major VARCHAR(10)
);

-- Insert Data

INSERT INTO students VALUES (1, 'Alice', 'CSE');
INSERT INTO students VALUES (2, 'Bob', 'ECE');
INSERT INTO students VALUES (3, 'Charlie', 'CSE');
INSERT INTO students VALUES (4, 'Rahul', 'CSE');


-- Create Enrollments Table
CREATE TABLE enrollments (
enrollment_id INT PRIMARY KEY,
student_id INT,
course_name VARCHAR(50),
fee INT
);

-- Insert Data

INSERT INTO enrollments VALUES (101, 1, 'Database Systems', 500);
INSERT INTO enrollments VALUES (102, 2, 'Embedded Systems', 450);
INSERT INTO enrollments VALUES (103, 3, 'Web Development', 400);
INSERT INTO enrollments VALUES (104, 99, 'Quantum Computing', 600);

-- =========================================
-- Query 1: SELECT
-- =========================================

SELECT *
FROM students;

-- =========================================
-- Query 2: WHERE
-- =========================================

SELECT student_name
FROM students
WHERE major = 'CSE';

-- =========================================
-- Query 3: INNER JOIN
-- =========================================

SELECT s.student_name,
e.course_name
FROM students s
INNER JOIN enrollments e
ON s.student_id = e.student_id;

-- =========================================
-- Query 4: LEFT JOIN
-- =========================================

SELECT s.student_name,
e.course_name
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id;

-- =========================================
-- Query 5: COUNT + GROUP BY
-- =========================================

SELECT major,
COUNT(*) AS total_students
FROM students
GROUP BY major;

-- =========================================
-- Query 6: SUM
-- =========================================

SELECT SUM(fee) AS total_fee
FROM enrollments;

-- =========================================
-- Query 7: AVG
-- =========================================

SELECT AVG(fee) AS average_fee
FROM enrollments;

-- =========================================
-- Query 8: HAVING
-- =========================================

SELECT major,
COUNT(*) AS total_students
FROM students
GROUP BY major
HAVING COUNT(*) > 1;

-- =========================================
-- Query 9: Subquery
-- =========================================

SELECT course_name,
fee
FROM enrollments
WHERE fee >
(
SELECT AVG(fee)
FROM enrollments
);

-- =========================================
-- Query 10: ORDER BY
-- =========================================

SELECT *
FROM enrollments
ORDER BY fee DESC;
