class Customer:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(customer):
    if customer.gender == "Male":
        print("Hello", cust.name, "sir") #similar to cust here customer is also a reference variable which is pointing to the object of class Customer
    else:
        print("Hello", cust.name, "ma'am")

cust = Customer("Ankita","Male") #cust is an reference variable which is pointing to the object of class Customer

greet(cust)