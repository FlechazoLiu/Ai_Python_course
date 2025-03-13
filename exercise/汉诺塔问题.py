step = 1
pole = ['a', 'b', 'c']

def move(n, from_pole, to_pole):
    global step
    if n > 1:
        move(n - 1, from_pole, 3 - from_pole - to_pole)
        move(1, from_pole, to_pole)
        move(n - 1, 3 - from_pole - to_pole, to_pole)
    elif n == 1:
        print(f"[step :{step}] from {pole[from_pole]} to {pole[to_pole]}")
        step += 1

n = int(input("请输入盘子的数量: "))

move(n, 0, 2)
print(step - 1)
