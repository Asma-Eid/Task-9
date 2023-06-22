
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self):
        return self.length * self.width

    def Perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Perimeter:", self.Perimeter())
        print("Area:", self.Area())
rec1 = Rectangle(7,13)
print(rec1.display())

class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


