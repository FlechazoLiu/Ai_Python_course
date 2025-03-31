def is_divisible(a):
    if type(a) != int:
        return "None"
    sum = 0
    num = abs(a)
    while num != 0:
        sum += num % 10
        num = num // 10
    if a % sum == 0:
        return 'Yes'
    else:
        return 'No'