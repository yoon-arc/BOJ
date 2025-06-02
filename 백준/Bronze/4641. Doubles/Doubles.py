while True:
    N = list(map(int, input().split()))
    if N[0] == -1:
        break
    N.sort()
    count = 0
    for i in range(1, len(N)):
        if N[i]*2 in N:
            count += 1
    print(count)