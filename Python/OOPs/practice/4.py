class Employee:
    def __init__(self,name,id,salary):
        self.employee_name=name
        self.employee_id=id
        self.employee_salary=salary

    def increment(self,percentage):
        self.incremented_salary=self.employee_salary+(self.employee_salary*percentage/100)
        return self.incremented_salary

emp1=Employee("Shubham",101,50000)
print(f"The Original Salary of {emp1.employee_name} is: {emp1.employee_salary}")
print(f"The Incremented Salary of {emp1.employee_name} is: {emp1.increment(10)} with a {10}% increase")  # Output: 55000.0
emp2=Employee("Ankita",102,60000)
print(f"The Original Salary of {emp2.employee_name} is: {emp2.employee_salary}")
print(f"The Incremented Salary of {emp2.employee_name} is: {emp2.increment(15)} with a {15}% increase")  # Output: 69000.0
