def sum_int_list(input_list, target):
    p = sorted(input_list)
    ls = []
    for num in p:
        if (target - num) in input_list:
            ls.append(tuple(sorted((input_list.index(num), input_list.index(target - num)))))
        else:
            continue
    ls.sort()
    return list(set(ls))

print(sum_int_list([-3, 3, -4, -8, 7], -1))