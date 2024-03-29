# Write your MySQL query statement below
SELECT Employees.employee_id
FROM Employees
LEFT JOIN Salaries
ON Employees.employee_id = Salaries.employee_id
WHERE name IS NULL OR salary IS NULL
UNION
SELECT Salaries.employee_id
FROM Salaries
LEFT JOIN Employees
ON Employees.employee_id = Salaries.employee_id
WHERE name IS NULL OR salary IS NULL
ORDER BY employee_id