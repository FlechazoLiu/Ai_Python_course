def count_sum_int_float(input_list):
    count, sum = 0, 0
    for item in input_list:
        if type(item) in (int, float):
            count +=1
            sum += item
    if count == 0:
        return (0,None)
    return (count, sum)


