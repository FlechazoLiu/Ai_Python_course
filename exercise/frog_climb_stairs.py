def frog_climb_stairs(N):
    ls = [1,1]
    for i in range(2,N+1):
        ls.append(ls[i-1]+ls[i-2])
    return ls[N]

print(frog_climb_stairs(100))