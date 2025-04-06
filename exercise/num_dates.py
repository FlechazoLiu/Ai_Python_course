def num_dates(a):
    # if (not a) or type(a) != list:
    #     return None
    if len(a) == 0:
        return None
    for item in a:
        if type(item) != int:
            return None
    r = []
    for i in range(len(a)):
        f = 0
        for j in range(len(a)):
            if i < j and a[j] > a[i]:
                r.append(j-i)
                f = 1
                break
        if not f:
            r.append(0)
    return r
