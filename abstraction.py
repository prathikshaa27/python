from abc import ABC, abstractmethod

class Shape(ABC):
    def area(self):
        pass
    def permiter(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
 

class Circle(Shape):
    def __init__(self,raduis):
        self.radius = raduis
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius

rectangle1 = Rectangle(3,5)
circle1= Circle(5)

print(rectangle1.area())
print(rectangle1.perimeter())
print(circle1.area())
print(circle1.perimeter())