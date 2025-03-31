def min_in_list_2(data):
    m1,m2 = 9999999,9999999
    i1,i2 = -1,-1
    for i in range(len(data)):
        if type(data[i]) == int or type(data[i]) == float:
            if data[i] < m1:
                m1,m2 = data[i],m1
                i1,i2 = i,i1
            elif data[i] < m2:
                m2 = data[i]
                i2 = i
    if i2 == -1:
        return None
    else:
        return (m2,i2)

print(min_in_list_2(["15.5", 7, 9, 2, -2, 2]))

