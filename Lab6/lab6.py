from turtle import*
import random

class Ball(Turtle):
    def __init__(self, radius, color, speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)
    

ball1 = Ball(15, 'red', 50)
ball2 = Ball(7, 'blue', 50)


def check_collision(ball1, ball2):
    D = math.sqrt(math.pow((ball2.xcor()-ball1.xcor1),2) + math.pow((ball2-ball1),2))
    if
