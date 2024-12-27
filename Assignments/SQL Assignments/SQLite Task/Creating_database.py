import sqlite3


conn=sqlite3.connect('D:\DownLoad\learining courses\DEPI-DS-AI\Assignments\SQL Assignments\SQLite Task\data\company.db')
cursor=conn.cursor()
cursor.execute("""Drop table if exists Employee""")
cursor.execute("""Drop table if exists Department""")


cursor.execute("""Create Table  Employee(
               employee_ID INTEGER PRIMARY KEY,
               name TEXT,
               LastName TEXT,  
               salary REAL,
               Manager_ID INTEGER,
               Department_ID INTEGER
               )""")


cursor.execute("""Create Table  Department(
                Department_ID INTEGER PRIMARY KEY,
                Department_Name TEXT
                )""")




cursor.execute("""INSERT INTO Employee (employee_ID, name, LastName, salary, Manager_ID, Department_ID) VALUES
(1, 'John', 'Doe', 2500, 101, 1),
(2, 'Jane', 'Smith', 3000, 200, 2),
(3, 'Mike', 'Brown', 4500, 102, 1),
(4, 'Anna', 'Taylor', 2800, 103, 3)
""")





cursor.execute("""INSERT INTO Department (Department_ID, Department_Name) VALUES
(1, 'HR'),
(2, 'Finance'),
(3, 'Engineering')""")


conn.commit()
cursor.close()

