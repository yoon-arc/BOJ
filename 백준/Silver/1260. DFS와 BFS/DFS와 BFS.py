from collections import deque
n,m,v = map(int, input().split())
#방문 기록
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)
#노드
node = [ [] for _ in range(n+1) ]
#리스트 입력
for _ in range(m):
    a,b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
#정렬 조심!
for i in node:
    i.sort()
#실질 계산
def dfs(s):
    dfs_visited[s] = True
    print(s, end = " ")
    for i in node[s]:
        if not dfs_visited[i]:
            dfs(i)
    
def bfs(s):
    q = deque([])
    q.append(s)
    while q:
        now = q.popleft()
        if not bfs_visited[now]:
            bfs_visited[now] = True
            print(now, end = " ")
            
            for i in node[now]:
                if not bfs_visited[i]:
                    q.append(i)

dfs(v)
print()
bfs(v)