def simplified_zigzag(l):
    le, wi = len(l), len(l[0])
    for item in l:
        if len(item) != wi:
            return []
    r = []
    
    for s in range(le+wi-1):
        for i in range(le):
            j = s - i
            if 0 <= j < len(l[0]): 
                r.append(l[i][j])
    return r