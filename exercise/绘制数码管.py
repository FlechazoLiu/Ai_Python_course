from turtle import *
from datetime import datetime
def drawLine():
    forward(50)
    left(90)

def drawNumber(num):
    draw_ls = [1] * 7
    draw_ls[0] = 0 if num in [0,1,7] else 1
    draw_ls[1] = 0 if num in [5,6] else 1
    draw_ls[2] = 0 if num in [1,4] else 1
    draw_ls[3] = 0 if num in [1,2,3,7] else 1
    draw_ls[4] = 0 if num in [1,3,4,5,7,9] else 1
    draw_ls[5] = 0 if num in [1,4,7,9] else 1
    draw_ls[6] = 0 if num in [2] else 1
    # print(draw_ls)
    for i in range(7):
        if i == 4:
            right(90)
        pendown() if draw_ls[i] else penup()
        drawLine()

    penup()
    left(180)
    forward(30)

def get_time():
    now = datetime.now()
    now_ls = now.strftime("%Y%m%d")
    now_ls = [int(c) for c in now_ls]
    return now_ls

def draw(now_ls):
    width, height = 800, 600
    setup(width=width, height=height)
    penup()
    goto(-(width/2-100),0)
    pendown()

    for i in now_ls:
        drawNumber(i)

    penup()


now = get_time()
draw(now)
mainloop()