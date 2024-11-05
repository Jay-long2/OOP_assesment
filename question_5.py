class Rectangle():
    def __init__(self,length,width):
        # If width is not provided, assume a square and set width equal to length
        if width is None:
            width = length
        self.length = length
        self.width = width

    
    def calculate_area(self):
        #Calculate the area of the rectangle.
        return self.length * self.width
    
# Creating a square (only one argument)
square = Rectangle(5,5)
print(print(f"Square area (5x5): {square.calculate_area()}") )

# Creating a rectangle (two arguments)
rectangle = Rectangle(5, 10)
print(f"Rectangle area (5x10): {rectangle.calculate_area()}") 