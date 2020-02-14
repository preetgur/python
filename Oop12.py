# Abstract base class and abstract method
# @abstractmethod : means this method is compulsary to define in every subclass
 
# For lower version : 
# from abc import ABCMeta, abstractmethod
# class Shape(metaclass=ABCMeta):

from abc import ABC, abstractmethod

class Shape(ABC):   
    # abstract base class : You cannot create the object of this class

    @abstractmethod
    def print_area(self):
        return 0

class Rectangle(Shape):
    tp = "Rectangle"
    side = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

# override method
    def print_area(self):
        return self.length * self.breadth 
           

rect1 = Rectangle()
print(rect1.print_area())

sh = Shape()   # object are not created