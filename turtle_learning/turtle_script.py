"""
Use the turtle module namespace
Using from turtle import * is convenient - but be warned that it imports a rather large collection of objects, 
and if you’re doing anything but turtle graphics you run the risk of a name conflict 
(this becomes even more an issue if you’re using turtle graphics in a script where other modules might be imported).

The solution is to use import turtle - fd() becomes turtle.fd(), 
width() becomes turtle.width() and so on. 
(If typing “turtle” over and over again becomes tedious, use for example import turtle as t instead.)
"""

import turtle as t
from random import random

for i in range(10):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

#The script will now wait to be dismissed and will not exit until it is terminated,
# for example by closing the turtle graphics window.
t.mainloop()