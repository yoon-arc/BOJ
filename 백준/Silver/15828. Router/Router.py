from collections import deque
dq = deque([])
N = int(input())
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        dq.popleft()
    if len(dq) < N and n != 0:
        dq.append(n)
if dq:
    print(*dq, end="")
else:
    print("empty")