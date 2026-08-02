#This is an example of polymorphism in Python, where the same method name can be used for different types of objects. In this case, we have two classes Dog and Cat, both having a method named sound, but they produce different outputs.
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
# Both classes Dog and Cat have a method named sound, but they produce different outputs. This is an example of polymorphism in Python, where the same method name can be used for different types of objects.

# -----------------------------------------------------------------------------------------------

#Through this example, we can see that Python supports polymorphism, allowing us to define methods with the same name in different classes, and the appropriate method is called based on the object type and the number of parameters given.
class Demo:

    def add(self,a,b):
        return a+b

    def add(self,a,b,c):
        return a+b+c

d=Demo()
print(d.add(1,2,3)) # This will call the second add method with three parameters, and python will use the last defined method with the same name, which takes three parameters. This is an example of method overloading in Python, where multiple methods can have the same name but different parameter lists.

# -----------------------------------------------------------------------------------------------

#Through this example, we can see that Python supports polymorphism and method overloading, allowing us to define methods with the same name but different behaviors based on the number of parameters passed.
class Demo:

    def add(self,a,b,c=0):
        return a+b+c

d = Demo()

print(d.add(2,3))

print(d.add(2,3,4))