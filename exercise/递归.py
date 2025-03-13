'''count = 0
def fact(n):
    global count
    count += 1
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
   # count += 1
fact(5)
print(count)'''

w = input('Enter a sentence: ')
for string in w:
    if string.lower() == 'u':
        string = '[omitted]'
print(w)