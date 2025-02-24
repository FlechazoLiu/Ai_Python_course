from turtle import *
color('green')
width(3)
forward(100)
left(120)
forward(100)
left(120)
forward(100)

up()
right(60)
forward(100)
down()

color('red')
forward(100)
left(120)
forward(100)
left(120)
forward(100)

up()
home()

clearscreen()

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)