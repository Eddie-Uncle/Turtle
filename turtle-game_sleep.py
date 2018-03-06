import turtle
from time import sleep

t = turtle.Turtle()
t.speed(0)


def square(length, angle):
    for i in range(4):
        t.forward(length)
        t.right(angle)


for i in range(10000):
    sleep(1)
    square(110, 90)
    t.right(20)