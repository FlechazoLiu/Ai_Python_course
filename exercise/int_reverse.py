def int_reverse(data):
    if type(data) != int:
        return None
    f = 1
    if data < 0:
        f = -1
    data = abs(data)
    rev = 0
    while data > 0:
        rev = rev * 10 + data % 10
        data = data // 10
    return rev * f

print(int_reverse(-10707))