class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
          # Ensure the other object is a Vector
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"vector {self.x} {self.y}"  

# Testing vector addition
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Adding two vectors
result = v1 + v2
print(result)  # Should print Vector(6, 8)
