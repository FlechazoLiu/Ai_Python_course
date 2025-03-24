def list_median(input_list):
    if not input_list:
        return None
    else:
        input_list.sort()
        if len(input_list) % 2 == 0:
            return (input_list[len(input_list) // 2] + input_list[len(input_list) // 2 - 1]) / 2
        else:
            return input_list[len(input_list) // 2]
print(list_median([2, 5, 3, 4]))
