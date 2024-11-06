from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Method to calculate area, to be implemented by subclasses."""
        pass

# Circle class that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Area of a circle: π * radius^2
        return math.pi * self.radius ** 2

# Square class that inherits from Shape
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        # Area of a square: side^2
        return self.side ** 2

# Demonstration
# Creating instances of Circle and Square
circle = Circle(5)  # Circle with radius 5
square = Square(4)  # Square with side length 4

# Calling area() on each instance
print("Circle area:", circle.area())  # Should print the area of the circle
print("Square area:", square.area())  # Should print the area of the square
