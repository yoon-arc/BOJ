P = int(input())
for _ in range(P):
    I = int(input())
    res = 0
    for j in range(1, I+1):
        res += j**2
    print(res)