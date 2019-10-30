import math

class Circle:
    def __init__(self, r):
        self.name = 'Круг'
        self.r = r

    def getSquare(self):
        s = math.pi * self.r**2
        return s

    def getPerimeter(self):
        p = 2 * math.pi * self.r
        return p

    def getName(self):
        return 'Circle'

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getSquare(self):
        return self.a * self.b 

    def getPerimeter(self):
        return (self.a + self.b) * 2

    def getName(self):
        return 'Rectangle'

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getSquare(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def getPerimeter(self):
        return (self.a + self.b + self.c) / 2

    def getName(self):
        return 'Triangle'
