def elementwise_product(x, y):
    r = []
    l = len(x)
    for a, b in zip(x,y):
        if type(a) == list:
            r.append(elementwise_product(a, b))
        else:
            r.append(a * b)
    return r

x, y = [1,2,3], [1,2,3]
print(elementwise_product(x, y))
