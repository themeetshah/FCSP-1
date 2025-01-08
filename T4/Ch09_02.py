# super()
print("\nsuper():")
class Parent:
    def __init__(self):
        print("Parent constructor")

    def show(self):
        print("Parent method")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

    def show(self):
        print("Child method")

c=Child()
c.show()  # Output: Child method
p=Parent()
p.show()  # Output: Parent method

# Overloading (Polymorphism)
# dunder methods (magic methods)
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self, other):
        # Subtraction: (a/b) - (c/d) = (ad - bc) / bd
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        # Multiplication: (a/b) * (c/d) = (ac) / (bd)
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        # Division: (a/b) / (c/d) = (ad) / (bc)
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __floordiv__(self, other):
        # Floor division: This is less common for fractions, but we can define it as integer division.
        return self.__truediv__(other).__trunc__()

    def __mod__(self, other):
        # Modulus operation: For fractions, this could be the remainder of the division.
        # This isn't always well-defined for fractions, so it may not be needed for basic Fraction class.
        raise NotImplementedError("Modulus operation is not defined for fractions.")

    def __pow__(self, other):
        # Exponentiation: Raising fraction to a power. 
        # (a/b) ** n = (a^n) / (b^n)
        if isinstance(other, int):
            new_numerator = self.numerator ** other
            new_denominator = self.denominator ** other
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Exponent must be an integer.")


# Method overloading isn't supported in py.
# Abstract class: 
# A class derived from abc is called abstract class in py. 
# Abstract class can have abstract methods and concrete methods.
# Abstract class methods need to be implemented.
# One can't create an instance of an abstract class.
# It is not necessary that every method in an abstract class is an abstract method.
# If there is any abstract method in a class, then that class must be abstract.
print("\nAbstract:")
from abc import ABC, abstractmethod
class Defense(ABC):
    def __init__(self):
        self.id=101
    
    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun is ready to fire")


class Army(Defense):
    def area(self):
        print("Land area")

class Airforce(Army):
    def area(self):
        print("Sky area")

class Navy(Army):
    def area(self):
        print("Sea area")

a=Army()
a.gun()