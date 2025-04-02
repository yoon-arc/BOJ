from collections import deque
#노드의 수, 에지의 수, 걸리는 거리, 출발 노드
N, M, K, X = map(int, input().split())
city = [[] for _ in range(N+1)]
visited = [-1]*(N+1)
ans = []

def bfs(v):
    dq = deque([])
    dq.append(v)
    visited[v] += 1
    while dq:
        now = dq.popleft()
        for i in city[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                dq.append(i)

for _ in range(M):
    s, e = map(int, input().split())
    city[s].append(e)

bfs(X)

for i in range(N+1):
    if visited[i] == K:
        ans.append(i)
if ans:
    ans.sort()
    for i in ans:
        print(i)
else:
    print(-1)
# print(city)