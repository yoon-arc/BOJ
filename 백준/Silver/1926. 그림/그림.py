from collections import deque
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
#방향
dhs, dys = [-1,0,1,0],[0,1,0,-1]
#큐
q = deque([])
max_drawing = 0
total = 0
#bfs
def bfs():
    global max_drawing
    count = 1
    while q:
        nh, ny = q.popleft()
        for i in range(4):
            ch, cy = nh+dhs[i], ny+dys[i]
            if 0<= ch < n and 0<= cy < m and paper[ch][cy]:
                paper[ch][cy] = 0 #방문 처리
                count += 1
                q.append((ch,cy))
    if count > max_drawing:
        max_drawing = count
for h in range(n):
    for y in range(m):
        if paper[h][y] == 1:
            q.append((h,y))
            paper[h][y] = 0 #방문 처리
            total += 1
            bfs()
print(total)
print(max_drawing)