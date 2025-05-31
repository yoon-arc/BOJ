# 1은 이동 가능, 0은 이동 x, (1,1)에서 시작해서 N,M까지 이동해야할 때 지나쳐야하는 최소 칸의 수
#시작 위치, 도착 위치도 카운트에 포함

from collections import deque
#방향
dhs, dys = [-1,0,1,0],[0,1,0,-1]
#입력
h, y = map(int, input().split())


#맵 입력
maze = [list(map(int, input().strip())) for _ in range(h)]

# 방문 배열 및 거리 배열 초기화,
visited = [[0]*y for _ in range(h)]
visited[0][0] = 1  # 시작 위치 방문 처리 및 거리 1

#큐
q = deque()
q.append((0,0))

while q:
    ch, cy = q.popleft()
        
    #방문한 적 없는 지, 범위 내 인지, 값이 1인지
    for nd in range(4):
        chd, cyd = ch+dhs[nd], cy+dys[nd]
        if  0 <= chd < h and 0<= cyd < y:
            if visited[chd][cyd] == 0 and maze[chd][cyd] == 1:
                visited[chd][cyd] = visited[ch][cy] + 1
                q.append((chd, cyd))
            
print(visited[h-1][y-1])   
