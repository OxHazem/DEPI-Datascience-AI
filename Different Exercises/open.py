class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  
        self.team_size = team_size

    def show_details(self):
        super().show_details() 
        print(f"Team Size: {self.team_size}")


employee = Employee("Ahmed", 5000)
manager = Manager("Sara", 10000, 5)


employee.show_details()
# Output: Name: Ahmed, Salary: 5000

manager.show_details()
# Output: 
# Name: Sara, Salary: 10000
# Team Size: 5 