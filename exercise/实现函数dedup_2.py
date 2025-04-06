# def dedup_2(list_a):
#     d = {}
#     ls = []
#     for a in list_a:
#         if a in d:
#             d[a] += 1
#         else:
#             d[a] = 1
#         if d[a] <= 2:
#             ls.append(a)
#     return ls

# print(dedup_2([1, 2, 3, 2, 3, 2, 1, 3, 5]))

def dedup_2(list_a):
    d = {}
    ls = []
    for a in list_a:
        d.setdefault(a, 0)
        d[a] += 1
        if d[a] <= 2:
            ls.append(a)
    return ls

print(dedup_2([1, 2, 3, 2, 3, 2, 1, 3, 5]))