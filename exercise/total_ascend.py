def total_ascend(h):
    count = 0
    x = 0
    l = len(h)
    while x < l:
        j = 1
        while x+j < l:
            if h[x+j-1] < h[x+j]:
                j += 1
            else:
                break
        if j != 1:
            count += 1
        x += j
    return count

print(total_ascend([100, 200, 150, 250]))