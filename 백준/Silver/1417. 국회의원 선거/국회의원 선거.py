N = int(input())
c = list(int(input()) for _ in range(N))
if N == 1:
    print(0)
else:
    count = 0
    while c[0] <= max(c[1:]):
        c[0] += 1
        c[c[1:].index(max(c[1:])) + 1] -= 1
        count += 1
    print(count)
