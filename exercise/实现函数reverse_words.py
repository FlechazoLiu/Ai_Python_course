def reverse_words(a):
    ls = a.split(' ')
    for i in range(len(ls)):
        ls[i] = ls[i][::-1]
    return ' '.join(ls)

print(reverse_words("hello world"))