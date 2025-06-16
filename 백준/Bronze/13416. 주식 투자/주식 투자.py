import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    days = int(input())
    total = 0
    for d in range(days):
        a,b,c = map(int, input().split())
        if a<0 and b <0 and c <0 :
            continue
        total += max(a,b,c)
    print(total)