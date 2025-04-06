def find_letter(a):
    if not a:
        return None
    ls = list(a)
    for item in ls:
        if ls.count(item) == 1:
            return (ls.index(item),item)