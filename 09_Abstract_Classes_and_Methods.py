from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,widht,hight):
        self.widht = widht
        self.hight = hight

    def area(self):
        return self.widht * self.hight   
rect = Rectangle(5,10)
print(f"Area of ranctangle:{rect.area()}")


