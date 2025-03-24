def abstract_value(a):
    if isinstance(a, (int, float)):
        return abs(a)
    else:
        try:
            t = float(eval(a))
            s = abs(t)
        except:
            s =  None

        return s
print(abstract_value('a'))
