import sys
input = sys.stdin.readline
N, M = map(int, input().split())
#노드
node = [ [] for _ in range(N+1)]
#방문 확인
visited = [False]*(N+1)
count = 0
#입력
for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

def dfs(s):
    stack = [s]
    visited[s] = True
    while stack:
        now = stack.pop()
        for nxt in node[now]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

for i in range(1, N+1):
    if not visited[i]:
        count += 1
        dfs(i)
print(count)