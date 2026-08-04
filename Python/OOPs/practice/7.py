class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

class Cow(Animal):
    def sound(self):
        print("Cow moos")

# Create instances of each class
dog=Dog()
cat=Cat()
cow=Cow()
