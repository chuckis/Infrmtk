import turtle
# import random

s = turtle.getscreen()
t = turtle.Turtle()
# t.shape("circle")
t.pen(pencolor="black", fillcolor="red", pensize=2, speed=9)
t.begin_fill()

n = 0
t.lt(60)
while n < 10:

    t.fd(20)
    t.rt(120)
    t.fd(20)
    t.lt(120)
    
    n+=1



