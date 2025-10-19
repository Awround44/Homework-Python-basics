from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def compare_area(self, other: 'Shape') -> str:
        if self.area() > other.area():
            return "larger"
        elif self.area() < other.area():
            return "smaller"
        return "equal"

    def compare_perimeter(self, other: 'Shape') -> str:
        if self.perimeter() > other.perimeter():
            return "larger"
        elif self.perimeter() < other.perimeter():
            return "smaller"
        return "equal"

class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return 4 * self.side

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

square = Square(4)
rectangle = Rectangle(5, 3)
triangle = Triangle(3, 4, 5)  # Right triangle for simplicity
circle = Circle(3)  # Radius of 3

print("Square:")
print(f"  Area: {square.area():.2f}")
print(f"  Perimeter: {square.perimeter():.2f}")

print("\nRectangle:")
print(f"  Area: {rectangle.area():.2f}")
print(f"  Perimeter: {rectangle.perimeter():.2f}")

print("\nTriangle:")
print(f"  Area: {triangle.area():.2f}")
print(f"  Perimeter: {triangle.perimeter():.2f}")

print("\nCircle:")
print(f"  Area: {circle.area():.2f}")
print(f"  Perimeter: {circle.perimeter():.2f}")

print("\nComparisons:")
print(f"Square area vs Rectangle area: {square.compare_area(rectangle)}")
print(f"Square perimeter vs Rectangle perimeter: {square.compare_perimeter(rectangle)}")