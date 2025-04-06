# def sum_int_list(input_list, target):
#     l = len(input_list)
#     ls = [(i,j) for i in range(l) for j in range(l) if i < j
#           and input_list[i]+input_list[j]==target]
#     ls.sort()
#     return ls

# print(sum_int_list([1,1], 2))

# 13'55

def sum_int_list(input_list, target):
    result = []
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if i < j and input_list[i] + input_list[j] == target:
                result.append((i,j))
    result = list(set(result))
    result.sort()
    return result

print(sum_int_list([-3, 3, -4, -8, 7], -1))