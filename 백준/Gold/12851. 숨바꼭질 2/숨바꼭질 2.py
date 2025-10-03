import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100001

dist = [-1] * MAX   # 최소 시간
ways = [0] * MAX    # 방법 수

q = deque([N])
dist[N] = 0
ways[N] = 1

while q:
    cur = q.popleft()
    for nxt in (cur-1, cur+1, cur*2):
        if 0 <= nxt < MAX:
            if dist[nxt] == -1:  # 처음 방문
                dist[nxt] = dist[cur] + 1
                ways[nxt] = ways[cur]
                q.append(nxt)
            elif dist[nxt] == dist[cur] + 1:  # 최단 거리 동일
                ways[nxt] += ways[cur]

print(dist[K])
print(ways[K])
