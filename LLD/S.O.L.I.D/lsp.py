"""
The Liskov Substitution Principle (LSP) is one of the SOLID principles of object-oriented design. 
It states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.
In other words, a subclass should behave in such a way that it does not break the functionality expected from the superclass.

The Liskov Substitution Principle ensures that inheritance is used correctly. 
Subclasses should extend the behavior of the superclass without altering its expected functionality. 
If a subclass cannot fully satisfy the superclass's contract, it may be better to use composition or a different design pattern.

Example of LSP Violation:
Let’s consider a classic example involving rectangles and squares. A square is a special type of rectangle, 
but if we model them incorrectly, we can violate LSP.

Problem:
A Rectangle has a set_width and set_height method.

A Square is a Rectangle where the width and height are always equal.

If we model Square as a subclass of Rectangle, we might violate LSP because changing the width of a square also changes its height, 
which is not the case for a rectangle.
"""


# (Violation of LSP):
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = width
        self.height = width  # Changing height to maintain square property

    def set_height(self, height):
        self.width = height
        self.height = height  # Changing width to maintain square property


# Function that works with Rectangle objects
def use_rectangle(rectangle: Rectangle):
    rectangle.set_width(5)
    rectangle.set_height(4)
    print(f"Expected area: 20, Actual area: {rectangle.area()}")


# Example usage
if __name__ == "__main__":
    rectangle = Rectangle(2, 3)
    use_rectangle(rectangle)  # Works as expected

    square = Square(2)
    use_rectangle(square)  # Violates LSP: Expected area 20, but actual area is 16


"""

Explanation of the Problem:
The use_rectangle function expects a Rectangle object and assumes that setting the width and height independently will work.

However, when a Square object is passed, setting the width also changes the height, violating the expected behavior of a Rectangle.

This breaks the Liskov Substitution Principle because Square cannot be substituted for Rectangle without altering the program's behavior.

Solution: Adhering to LSP
To adhere to LSP, we need to ensure that subclasses (e.g., Square) do not alter the behavior expected from the superclass (e.g., Rectangle). One way to do this is to avoid inheritance if the subclass cannot fully satisfy the superclass's contract.

Refactored Design:
Instead of making Square a subclass of Rectangle, we can create a separate class hierarchy or use composition.

"""

from abc import ABC, abstractmethod


# Abstract base class for shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


# Square class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def set_side(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Function that works with Shape objects
def use_shape(shape: Shape):
    if isinstance(shape, Rectangle):
        shape.set_width(5)
        shape.set_height(4)
    elif isinstance(shape, Square):
        shape.set_side(4)
    print(f"Area: {shape.area()}")


# Example usage
if __name__ == "__main__":
    rectangle = Rectangle(2, 3)
    use_shape(rectangle)  # Area: 20

    square = Square(2)
    use_shape(square)  # Area: 16
