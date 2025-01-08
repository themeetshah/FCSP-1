from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def __gt__(self, other):
        return self.l * self.b > other.l * other.b

    def calculate_area(self):
        return self.l*self.b

class Circle(Shape):
    def __init__(self,r):
        self.r=r
        
    def calculate_area(self):
        return f"{((math.pi)*(self.r)**2):.2f}"
    
r1=Rectangle(2,3)
r2=Rectangle(3,3)
c=Circle(3)
print("Area of rect1:",r1.calculate_area())
print("Area of rect2:",r2.calculate_area())
print("Area of circle:",c.calculate_area())
print("MRO of circle:",Circle.mro())
print("Rect1>Rect2?:",r1>r2)
print("Rect2>Rect1?:",r2>r1)