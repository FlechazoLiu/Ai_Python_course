ls = ['caabb', 'aabbb', 'abc', 'aabbcc', 'ab']
ls.sort(key=lambda x: (-x.count('a'), x))
print(ls)