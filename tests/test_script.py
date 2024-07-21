#!/usr/bin/env python

"""A simple script to calculate Fibonacci numbers. After
the number is calculated, ti is going to be returned as a number
"""

def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
      return fibonacci(n - 1) + fibonacci(n - 2)

class Shape:
    """A class to represent a geometric shape."""

    def __init__(self, name):
        """Initialize the Shape object with a name."""
        self.name = name

    def area(self):
        pass

if __name__ == "__main__":
    print("Fibonacci sequence:")
    for i in range(10):
        print(fibonacci(i))

    # create a shape object
    shape = Shape("Square")
    print("Name of the shape:", shape.name)
