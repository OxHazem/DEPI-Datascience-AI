import sqlite3


conn=sqlite3.connect("D:\DownLoad\learining courses\DEPI-DS-AI\Assignments\SQL Assignments\SQLite Task\data\company.db")
cursor=conn.cursor()
# Question: 
# Write a SQL query to retrieve the emp_id, last_name, and salary of employees whose salary is 
# between 2,000 and 5,000 and do not have a manager ID of 101 or 200.
cursor.execute("""SELECT employee_ID ,LastName, salary 
               FROM Employee
               Where salary Between 2000 AND 5000 AND Manager_ID NOT IN (101,200)""")

print(cursor.fetchall())

# Question: 
# Write a SQL query to display the employee names along with their respective department names. 
# Use aliases for table names for better readability. 

cursor.execute("""Select Employee.name  , Department.Department_Name  From Employee   join Department ON Employee.Department_ID = Department.Department_ID    ORDER BY Department.Department_Name ASC""")

print(cursor.fetchall())


# Question: 
# Write a SQL query to find the number of employees and the average salary for each department. 
# Ensure that the results are grouped by department ID.

cursor.execute("""Select Count(Employee.employee_ID),AVG(salary),Department_ID From Employee  Group by Department_ID""")
print(cursor.fetchall())








