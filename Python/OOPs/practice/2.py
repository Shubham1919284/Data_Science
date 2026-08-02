class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

obj=Rectangle(5,10)
print(f"Area of rectangle is: {obj.area()}")
print(f"Perimeter of rectangle is: {obj.perimeter()}")