-- Create the database

CREATE DATABASE CompanyDB;


-- Connect to the database



-- Create the departments table

CREATE TABLE departments (

department_id SERIAL PRIMARY KEY,

department_name VARCHAR(100) NOT NULL

);


-- Create the employees table

CREATE TABLE employees (

employee_id SERIAL PRIMARY KEY,

employee_name VARCHAR(100) NOT NULL,

salary NUMERIC(10, 2) NOT NULL,

department_id INT REFERENCES departments(department_id)

);


SELECT * FROM departments



