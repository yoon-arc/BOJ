import sys
input = sys.stdin.readline
n = int(input())
nums = list(int(input()) for _ in range(n))
ans = []
stack = []
current = 1
able = True

for i in nums:
    while current <= i:
        stack.append(current)
        ans.append('+')
        current += 1
    if stack[-1] == i :
        ans.append('-')
        stack.pop()
    else:
        able = False
        break
if not able:
    print('NO')
else:
    print("\n".join(ans))