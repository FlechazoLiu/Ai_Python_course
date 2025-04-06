def count_characters(string):
    ls = list(string.lower())
    d = {}
    r = []
    for word in ls:
        d.setdefault(word,0)
        d[word] += 1
    for word, count in d.items():
        r.append('{0}:{1}'.format(word,count))
    r.sort()
    return ', '.join(r)

print(count_characters("zzAAAbb") )