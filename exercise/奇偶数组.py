'''
ls = [1,2,3,4,5,6,7,8,9]
w = []
for i in ls:
    if i % 2 != 0:
        w.append(i)
print(w)
'''

str = '    hello   world    hei  '
ls = str.split()
for i in range(len(ls)-1):
    print(ls[i], end=' ')
print(ls[len(ls)-1])