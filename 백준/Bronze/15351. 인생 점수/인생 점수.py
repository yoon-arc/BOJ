N = int(input())
for _ in range(N):
    total = 0
    c = input().replace(" ","")
    for n in c:
        total += (ord(n)-64)
    if total == 100:
        print('PERFECT LIFE')
    else:
        print(total)