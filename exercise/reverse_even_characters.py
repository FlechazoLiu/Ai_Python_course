def reverse_even_characters(string):
    ls = list(string)
    even = ls[1::2]
    even.reverse()
    ls[1::2] = even
    return "".join(ls)
