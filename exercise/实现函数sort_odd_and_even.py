def sort_odd_and_even(a):
    if type(a) != list:
        return None
    if len(a) == 0:
        return []
    for x in a:
        if type(x) != int:
            return None
    ls1,ls2 = [],[]
    for x in a:
        if x % 2 == 1:
            ls1.append(x)
        else:
            ls2.append(x)
    ls1.sort(reverse=True)
    ls2.sort()
    return ls1 + ls2

print(sort_odd_and_even([1, 2, 3, 4, 5]))