from collections import deque
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
#방향
dhs, dys = [-1,0,1,0],[0,1,0,-1]
#큐
q = deque([])
max_drawing = 0
total = 0
#범위 체크
def in_range(h,y):
    return 0<= h < n and 0<= y < m
    
#bfs
def bfs():
    global total
    global max_drawing
    count = 1
    total += 1
    while q:
        nh, ny = q.popleft()
        visited[nh][ny] = 1
        for i in range(4):
            ch, cy = nh+dhs[i], ny+dys[i]
            if in_range(ch,cy) and paper[ch][cy] and not visited[ch][cy]:
                count += 1
                visited[ch][cy] = 1
                q.append((ch,cy))
    if count > max_drawing:
        max_drawing = count
        

for h in range(n):
    for y in range(m):
        if paper[h][y] == 1 and not visited[h][y]:
            q.append((h,y))
            bfs()

print(total)
print(max_drawing)