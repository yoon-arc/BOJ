import sys
lines = sys.stdin.readlines()
ans = 0
for i in lines:
    ans += int(i)
print(ans)