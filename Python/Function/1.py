# def hello(name):
#     print(f"Hello, {name}!")

# hello("Alice")

def hello(name,age):
    print(f"Hello, {name}! You are {age} years old.")

hello(age=30, name="Alice") #This represents a function call with keyword arguments, where the order of the arguments does not matter.

def hello(name="World", age=0):
    print(f"Hello, {name}! You are {age} years old.")

hello() #This represents a function call with default arguments, where the default values are used if no arguments are provided.
hello("Bob") #This represents a function call with a positional argument, where the default value for age is used.
hello("Charlie", 25) #This represents a function call with both positional arguments, where the provided values are used.