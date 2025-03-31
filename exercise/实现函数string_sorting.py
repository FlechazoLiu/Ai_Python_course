def string_sorting(string_list):
    pos_ls = []
    str_ls = []
    for i in range(len(string_list)):
        if type(string_list[i]) == str:
            pos_ls.append(i)
            str_ls.append(string_list[i])
    str_ls.sort()
    for i in range(len(str_ls)):
        string_list[pos_ls[i]] = str_ls[i]
    return string_list
