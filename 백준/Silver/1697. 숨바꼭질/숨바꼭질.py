from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100000
visited = [0] * (MAX + 1)

def bfs(start):
    dq = deque([start])
    while dq:
        now = dq.popleft()
        if now == K:
            return visited[now]
        for nxt in (now-1, now+1, now*2):
            if 0 <= nxt <= MAX and visited[nxt] == 0:
                visited[nxt] = visited[now] + 1
                dq.append(nxt)

print(bfs(N))
