from turtle import *
colormode(255)

##class Square(Turtle):
##    def __init__(self, size):
##        Turtle.__init__(self)
##        self.shapesize(size)
##        self.shape("square")
##
##sq  = Square(10)

class Rectangle(Turtle):
    def __init__(self, width, height):
        Turtle.__init__(self)
        self.penup()
        self.begin_poly()
        self.fd(width)
        self.left(90)
        self.fd(height)
        self.left(90)
        self.fd(width)
        self.left(90)
        self.fd(height)
        self.left(90)
        self.end_poly()
        r1 = self.get_poly()
        register_shape("Rectangle", r1)
        self.shape("Rectangle")
r1 = Rectangle(200, 80)

##class Square(Rectangle):
##    def __init__(self):


##class Hexagon(Turtle):
##    def __init__(self, size, color, age):
##        Turtle.__init__(self)
##        self.penup()
##        self.begin_poly()
##        self.fd(size)
##        self.left(60)
##        self.fd(size)
##        self.left(60)
##        self.fd(size)
##        self.left(60)
##        self.fd(size)
##        self.left(60)
##        self.fd(size)
##        self.left(60)
##        self.fd(size)
##        self.left(60)
##        self.end_poly()
##        h1 = self.get_poly()
##        register_shape("Hexagon", h1)
##        self.shapesize(size)
##        self.shape("Hexagon")
##        self.color(color)
##        self.age(age)
##h1 = Hexagon(7,"red", 8)
##
