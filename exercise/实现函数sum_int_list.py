def sum_int_list(input_list, target):
    l = len(input_list)
    ls = [(i,j) for i in range(l) for j in range(l) if i < j
          and input_list[i]+input_list[j]==target]
    ls.sort()
    return ls

print(sum_int_list([1,1], 2))

# 13'55