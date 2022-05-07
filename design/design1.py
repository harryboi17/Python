from turtle import *

bgcolor('black')
speed(0)
hideturtle()

for i in range(90):
    color('red')
    circle(i)
    color('orange')
    circle(i*0.8)
    right(4)
    forward(4)
done()