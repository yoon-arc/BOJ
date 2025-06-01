from collections import deque
N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
visited = [ [0] * M for _ in range(N)]
max_val = -100000

#방향(시계 방향)
dhs, dys = [-1,-1,-1,0,1,1,1,0],[-1,0,1,1,1,0,-1,-1]

#큐
q= deque([])


def in_range(h,y):
    return 0<= h < N and 0<= y < M

def bfs():
    global max_val
    while q:
        nh, ny = q.popleft()
        for i in range(8):
            ch, cy = nh+dhs[i],ny+dys[i]
            #거리 측정
            if in_range(ch,cy) and sea[ch][cy] == 0 and visited[ch][cy] == 0:
                visited[ch][cy] = visited[nh][ny] + 1
                if visited[ch][cy] > max_val:
                    max_val = visited[ch][cy]
                q.append((ch,cy))

#1이 걸리지 않는 이상
for h in range(N):
    for y in range(M):
        if sea[h][y] == 1 :
            q.append((h,y))
bfs()

print(max_val)
                    