from turtle import *

def koch(dim,length):
    if dim == 0:
        forward(length)
    else:
        koch(dim-1,length/3)
        left(60)
        koch(dim-1,length/3)
        right(120)
        koch(dim-1,length/3)
        left(60)
        koch(dim-1,length/3)

def draw():
    w, h = 800, 800
    n = eval(input("你要生成科赫曲线的迭代阶数:"))
    setup(w,h)
    penup()
    speed(10)
    goto(-(w/2-100),w/5)
    pendown()

    koch(n,w-200)
    right(120)
    koch(n,w-200)
    right(120)
    koch(n,w-200)


    mainloop()

draw()