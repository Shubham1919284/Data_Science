class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age  

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks

    def display(self):
        super().display()
        print(f"Marks: {self.marks}")

stu1=Student("Shubham",21,[90,80,70])
stu1.display()