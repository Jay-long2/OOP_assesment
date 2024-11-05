class Calculator:
    count = 0  # Static attribute to track the number of times add() is called

    @staticmethod
    def add(a, b):
        Calculator.count += 1  # Increment the count each time add() is called
        return a + b

# Demonstration
print("Sum:", Calculator.add(5, 3))  # Should print "Sum: 8"
print("Count after first call:", Calculator.count)  # Should print 1

print("Sum:", Calculator.add(10, 15))  # Should print "Sum: 25"
print("Count after second call:", Calculator.count)  # Should print 2

print("Sum:", Calculator.add(2.5, 4.5))  # Should print "Sum: 7.0"
print("Count after third call:", Calculator.count)  # Should print 3
