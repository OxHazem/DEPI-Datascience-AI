CREATE TABLE  employees(
employee_id SERIAL PRIMARY KEY,
fname varchar(50),
lname varchar(50),
salary Real,
manager_id INTEGER,
department_id INTEGER

);

CREATE TABLE departments(
    department_id SERIAL PRIMARY KEY,
    dname Text
);


CREATE TABLE suppliers(
suplier_id SERIAL PRIMARY KEY,
name VARCHAR(50),
status INTEGER
);




INSERT INTO employees (fname, lname, salary, manager_id, department_id) VALUES
('John', 'Doe', 2500, 101, 1),
('Jane', 'Smith', 3000, 200, 2),
('Mike', 'Brown', 4500, 102, 1),
('Anna', 'Taylor', 2800, 103, 5);

INSERT INTO departments (dname) VALUES
('HR'),
('Finance'),
('Engineering');

INSERT INTO suppliers (name, status) VALUES
('Supplier A', 20),
('Supplier B', 10),
('Supplier C', 30);
