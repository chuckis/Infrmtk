import turtle
import random

s = turtle.getscreen()
t = turtle.Turtle()
# t.shape("circle")
t.pen(pencolor="black", fillcolor="red", pensize=2, speed=9)
# t.begin_fill()
# t.fd(100)
# t.lt(120)
# t.fd(100)
# t.lt(120)
# t.fd(100)
n = 10
while n <= 800:
    # t.circle(n)
    t.fd(random.randrange(30, 100))
    t.rt(random.randrange(90, 270, 45))
    n+=10


# t.end_fill()

