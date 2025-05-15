n = int(input())
c,j = 100,100
for _ in range(n):
    a,b = map(int, input().split())
    if a == b:
        continue
    if a > b :
        j -= a
    else:
        c -= b
print(c)
print(j)