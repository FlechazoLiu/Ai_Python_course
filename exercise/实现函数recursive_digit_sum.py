def recursive_digit_sum(a):
    if a <= 9:
        return a
    else:
        sum = 0
        while a != 0:
            sum += a % 10
            a = a // 10
        return recursive_digit_sum(sum)
print(recursive_digit_sum(88888888888888))