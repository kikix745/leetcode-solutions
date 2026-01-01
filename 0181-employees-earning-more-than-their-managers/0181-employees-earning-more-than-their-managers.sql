# Write your MySQL query statement below
SELECT 
    e.name as employee
FROM employee e
LEFT JOIN employee m
    ON e.managerId = m.id
 where m.salary<e.salary ;  