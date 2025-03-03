import math
# try:
#     a = eval(input("输入一个整数："))
#     print(type(a))
#     print(a,end="tt")
# except:
#     print("这不是一个整数")


#s1=0
#s2=0
#while 4*math.fabs(s1-s2)>0.01:

s=0
r=1
for i in range(100000):
    s = s + 1 / (2*i + 1) * r
    r = - r
    print(4 * s)