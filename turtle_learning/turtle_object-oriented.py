from turtle import Turtle
from random import random

t = Turtle()

t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("orange")

for i in range(10):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()