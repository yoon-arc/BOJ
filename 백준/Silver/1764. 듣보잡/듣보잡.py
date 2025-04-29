import sys
input = sys.stdin.readline
N, M = map(int, input().split())
N_name, M_name = set(),set()
for _ in range(N):
    N_name.add(input().strip())
for _ in range(M):
    M_name.add(input().strip())
ans = sorted(N_name & M_name)
print(len(ans))
for i in ans:
    print(i)