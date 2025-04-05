a = input("主串:")
b = input("子串:")
l = len(b)
find = []
for i in range(len(a)):
    if a[i:i+l] == b:
        find.append(i)
print(find[len(find)-2] if len(find) > 0 else -1)