import math
oper_dict = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    'sin': lambda x: math.sin(x),
    'cos': lambda x: math.cos(x),
    'tan': lambda x: math.tan(x),
    'asin': lambda x: math.asin(x),
    'atan': lambda x: math.atan(x),
    'exp': lambda x: math.exp(x),
    'ln': lambda x: math.log(x),
    'log10': lambda x: math.log10(x)
}

while True:
    s = input("请输入一个前缀表达式,运算符和数字间用空格分开(输入空字符退出):")
    if len(s) < 1:
        break
    tokens = s.split()
    oper = oper_dict[tokens[0]]
    operand = []
    for token in tokens[1:]:
        operand.append(float(token))
    out = oper(*operand)
    print(out)