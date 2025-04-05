arr = [1,2,3,4,5,6,7,8,9]
arr_str = list(map(str, arr))
arr_str.reverse()
result = '-'.join(arr_str)
print(result)