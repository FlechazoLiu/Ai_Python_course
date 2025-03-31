def password_check(a):
    s = 1
    if type(a) != str:
        return False
    if len(a) < 6 or len(a) > 12:
        s = 0
    ls = [0,0,0]
    for x in a:
        if x.isupper():
            ls[0] = 1
        if x.islower():
            ls[1] = 1
        if x.isdigit():
            ls[2] = 1
    if 0 in ls:
        s = 0
    if "$" not in a and "@" not in a and "#" not in a:
        s = 0
    return True if s == 1 else False

print(password_check(123))