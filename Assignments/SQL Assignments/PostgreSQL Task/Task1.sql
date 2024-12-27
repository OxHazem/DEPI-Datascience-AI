-- Question: 
-- Create a simple view named vw_employee_details that displays the first name, last name, and 
-- department name of employees.

-- CREATE VIEW  Q1  AS 
-- SELECT fname ,lname , departments.dname 
-- From employees join departments on  employees.department_id = departments.department_id ;

-- SELECT * FROM Q1 

-- Question: 
-- Modify the existing view vw_work_hrs to only include employees working in department 
-- number 5.


-- CREATE OR REPLACE VIEW vw_work_hrs AS


-- SELECT employees.fname, employees.lname, departments.dname AS pname, employees.salary AS hours
-- FROM employees 
-- JOIN departments 
-- ON employees.department_id = departments.department_id
-- WHERE employees.department_id = 5;

-- SELECT * FROM vw_work_hrs ;


-- Question: 
-- Create a view named vw_high_status_suppliers to display all suppliers with a status greater 
-- than 15, and ensure that any updates or inserts through the view still meet the status condition.

-- CREATE VIEW Q3 AS 
-- SELECT *
-- FROM suppliers
-- WHERE status > 15
-- With CHECK OPTION;

-- SELECT * FROM Q3




