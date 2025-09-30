N, M = map(int, input().split())
graph = [ [] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
times = 0


for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)



def dfs(start_node):
    for i in graph[start_node]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)


for i in range(1, N + 1):
    if visited[i] == False:
        times += 1
        dfs(i)
       
        



start_node = 1
visited[start_node] = True
dfs(start_node)
print(times)