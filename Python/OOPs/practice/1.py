class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")

stu1=Student("Shubham",21,[90,80,70])
stu1.display()
