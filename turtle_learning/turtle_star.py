from turtle import *
color('red')
fillcolor('yellow')
begin_fill()      #filling can be turned on and off:
while True:
    fd(200)       #fd()==forward()
    left(170)
    if abs(pos()) < 1:     #abs(pos()) < 1 is a good way to know when the turtle is back at its home position.
        break
end_fill()        #(Note that filling only actually takes place when you give the end_fill() command.)