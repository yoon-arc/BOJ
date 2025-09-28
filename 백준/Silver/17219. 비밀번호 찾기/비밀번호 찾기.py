import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pwds = {}
for _ in range(N):
    s, p = input().split()
    pwds[s] = p
for _ in range(M):
    q = input().rstrip()
    print(pwds[q])