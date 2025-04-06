def max_in_list(data):
    max = -999999
    for item in data:
        if type(item) == int or type(item) == float:
            if item > max:
                max = item
        elif type(item) == tuple or type(item) == list or type(item) == set:
            item = list(item)
            temp = max_in_list(item)
            if temp > max:
                max = temp
    if max == -999999:
        return None
    else:
        return max

print(max_in_list(["15.5", 7, [(9,2),-2]]))