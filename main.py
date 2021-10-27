import math

from copy import copy

class Point:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
    def __copy__(self):
        return

    def distance(self, other):
        delta_x = self.x1 - other.x1
        delta_y = self.y1 - other.y1
        return (delta_x ** 2 + delta_y ** 2) ** 0.5

x1, y1, x2, y2 = [int(x) for x in input("Введи координаты 2-ух точек").split()]

point1 = Point(x1, y1)
point2 = Point(x2,y2)
Distance = point1.distance(point2)
print(Distance)

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def perimeter(self):
        return a + b + c

    def area(self):
        return math.sqrt(p * (p - a) * (p - b) * (p - c))



x3,y3 = [int(x) for x in input("Введи координаты").split()]

point3 = Point(x3,y3)

a = point1.distance(point2)
b = point2.distance(point3)
c = point3.distance(point1)

triangle = Triangle(a, b, c)

p = triangle.perimeter()

s = triangle.area()
print("Периметр треугольника:", p)
print("Площадь треугольника:", s)
class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def perimeter(self):
        return math.pi * radius

    def area(self):
        return math.pi * radius**2



radius = int(input("Задай радиус"))

centre = point1
circle = Circle(centre, radius)
p_circle = circle.perimeter()
s_circle = circle.area()
print("Периметр окружности:", p_circle)
print("Площадь окружности:", s_circle)
x4,y4 = [int(x) for x in input("Введи координаты точки").split()]
point4 = Point(x4,y4)
if radius < centre.distance(point4):
    print("Вне окружности")
else:
    print("Внутри окружности")
x5, y5 = [int(x) for x in input("Введи координаты центра второй окружности").split()]
centre2 = Point(x5, y5)
radius2 = int(input("Введи радиус второй окружности"))
circle2 = Circle(centre2, radius2)
if radius + radius2 < centre.distance(centre2) and centre2.distance(point4) < radius:
    print("Не пересекаются")
else:
    print("Пересекаются")



