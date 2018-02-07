import turtle
import time
import random
import math
from ball import Ball

turtle.tracer (0)
turtle.hideturtle()
running = True
sleep = 0.0077
screen_width = round(turtle.getcanvas().winfo_height()/2)
screen_height = round(turtle.getcanvas().winfo_height()/2)


NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

myball = Ball(0, 0 , 100, 100, 120, "red")

BALLS = []
for i in range (NUMBER_OF_BALLS):
    x = random.randint(-screen_width + MAXIMUM_BALL_RADIUS, screen_width - MAXIMUM_BALL_RADIUS)
    y = random.randint(-screen_height + MAXIMUM_BALL_RADIUS, screen_height - MAXIMUM_BALL_RADIUS)
    dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
    dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
    r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
    color = (random.random(), random.random(), random.random())
    ball=Ball(x, y, dx, dy, r, color)
    BALLS.append(ball)

def move_all_balls():
    for i in BALLS:
        i.move(screen_width, screen_height)

def collide(ball_a, ball_b):
   ##print (ball_a.pos(),ball_b.pos())
    if ball_a.pos() == ball_b.pos():
        return False
    d = math.sqrt(math.pow((ball_b.xcor()-ball_a.xcor()),2) + math.pow((ball_b.ycor()-ball_a.ycor()),2))
    if d <= ball_a.r + ball_b.r:
        return True
    return False

def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            if collide(ball_a, ball_b) == True:
                if ball_a.r > ball_b.r:
                    ball_a.r=+1
                    ball_b.x = random.randint(-screen_width + MAXIMUM_BALL_RADIUS, screen_width - MAXIMUM_BALL_RADIUS)
                    ball_b.y = random.randint(-screen_height + MAXIMUM_BALL_RADIUS, screen_height - MAXIMUM_BALL_RADIUS)
                    ball_b.goto(x, y)
                    ball_b.dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                    ball_b.yx = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                    ball_b.r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
                    ball_b.shapesize(random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)/10)
                    ball_b.color = (random.random(), random.random(), random.random())
                else:
                    ball_b.r=+1
                    ball_a.x = random.randint(-screen_width + MAXIMUM_BALL_RADIUS, screen_width - MAXIMUM_BALL_RADIUS)
                    ball_a.y = random.randint(-screen_height + MAXIMUM_BALL_RADIUS, screen_height - MAXIMUM_BALL_RADIUS)
                    ball_a.goto(x, y)
                    ball_a.dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                    ball_a.yx = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                    ball_a.r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
                    ball_a.shapesize(random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)/10)
                    ball_a.color = (random.random(), random.random(), random.random())
def check_myball_collision():
    for ball in BALLS:
        if collide(myball, ball) == True:
            print("Collided")
            if myball.r>ball.r:
                myball.r+=1
                myball.shapesize(myball.r/10)
                ball.x = random.randint(-screen_width + MAXIMUM_BALL_RADIUS, screen_width - MAXIMUM_BALL_RADIUS)
                ball.y = random.randint(-screen_height + MAXIMUM_BALL_RADIUS, screen_height - MAXIMUM_BALL_RADIUS)
                ball.goto(ball.x, ball.y)
                ball.dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                ball.dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                ball.r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
                ball.shapesize(random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)/10)
                ball.color = (random.random(), random.random(), random.random())
            else:
                return False
    return True
##check_myball_collision()

def movearound(event):
    myball.goto(event.x - screen_width, screen_height - event.y)


turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()
RUNNING = True
while RUNNING:
    if (screen_width != turtle.getcanvas().winfo_width()/2 or screen_height != turtle.getcanvas().winfo_height()/2):
        screen_width = round(turtle.getcanvas().winfo_width()/2)
        screen_height = round(turtle.getcanvas().winfo_height()/2)
    move_all_balls()
    check_all_balls_collision()
    RUNNING = check_myball_collision()
    turtle.getscreen().update()
    time.sleep(sleep)


turtle.mainloop()
