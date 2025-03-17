import random
import math
def leibniz(rounds):
    s = 0
    r = 1
    for i in range(rounds):
        s = s + 1 / (2 * i + 1) * r
        r = - r
        if i in show:
            print("round:",i , 4 * s )

def Monte_Carlo(rounds):
    hits = 0
    for i in range(1, rounds + 1):
        x,y = random.random(), random.random()
        r = math.sqrt(x * x + y * y)
        if r < 1:
            hits += 1
        if i in show:
            print("round:",i,4 * hits / i)

def Nilakantha(rounds):
    s = 3
    r = 1
    for i in range(1, rounds + 2):
        s += 4 / (2*i * (2*i + 1) * (2*i + 2)) * r
        r = - r
        if i in show:
            print("round:",i,s)


def func(choice,p):
    global name
    if choice == 1:
        f = leibniz

    elif choice == 2:
        f = Monte_Carlo

    elif choice == 3:
        f = Nilakantha

    f(p)


show = [1,10,20,50,100,200,500,1000,10000,15000,50000,100000]
choice = int(input("Which method do you use(1 for leibniz/2 for Monte Carlo/3 for Nilakantha):"))
p = int(input("How many rounds do you want:"))
print("pi is around:")

func(choice,p)