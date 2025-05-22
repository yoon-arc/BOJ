T = int(input())
for _ in range(T):
    s = int(input())
    n = int(input())
    if n == 0:
        print(s)
        continue
    for i in range(n):
        q, p = map(int, input().split())
        s += q*p
    print(s)