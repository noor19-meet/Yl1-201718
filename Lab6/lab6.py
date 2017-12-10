from turtle import*
import random
import math

class Ball(Turtle):
    def __init__(self, radius, color, speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)
    

ball1 = Ball(15, 'red', 50)
ball2 = Ball(12, 'blue', 50)


##def check_collision(ball1, ball2):
##    D = math.sqrt(math.pow((ball2.xcor()-ball1.xcor()),2) + math.pow((ball2.ycor() -ball1.ycor()),2))
##    if D <= ball1.radius + ball2.radius:
##       print("collision")
## check_collision(ball1, ball2)


balls = []
balls.append(ball1)
balls.append(ball2)

def ball_s (balls):
    D = math.sqrt(math.pow((balls[1].xcor()-balls[0].xcor()),2) + math.pow((balls[1].ycor() -balls[0].ycor()),2))
    if D <= balls[0].radius + balls[1].radius:
        if balls[0].radius < balls[1].radius:
            balls[0].goto(70, 80)
        else:
            balls[1].goto(50, 90)

ball_s(balls)
