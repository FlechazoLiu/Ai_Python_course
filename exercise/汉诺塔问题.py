step = 1
pole = ['a', 'b', 'c']
plate = [[0] * 15 for _ in range(3)]

def move(n, from_pole, to_pole):
    global step
    if n > 1:
        move(n - 1, from_pole, 3 - from_pole - to_pole)
        move(1, from_pole, to_pole)
        move(n - 1, 3 - from_pole - to_pole, to_pole)
    elif n == 1:
        for j in range(14, -1, -1):
            if plate[from_pole][j] != 0:
                print(f"[step :{step}] move plate {plate[from_pole][j]}# from {pole[from_pole]} to {pole[to_pole]}")
                step += 1
                temp = plate[from_pole][j]
                plate[from_pole][j] = 0


                for m in range(14, -1, -1):
                    if plate[to_pole][m] != 0:
                        plate[to_pole][m + 1] = temp
                        break
                    elif m == 0:
                        plate[to_pole][m] = temp
                        break
                break



n = int(input("请输入盘子的数量: "))
for i in range(n):
    plate[0][i] = n - i

move(n, 0, 2)
print(step - 1)
