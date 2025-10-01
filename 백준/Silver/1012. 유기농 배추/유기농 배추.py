from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
dh, dy = [-1,0,1,0],[0,1,0,-1]
#함수(범위 검사, bfs)
def in_range(h,y,H,Y):
    return 0<=h<H and 0<=y<Y

def bfs(h,y):
    global count
    dq = deque([])
    dq.append((h,y))
    visited[h][y] = 1
    while dq:
        nh, ny = dq.popleft()
        for i in range(4):
            cnh, cny = nh+dh[i], ny+dy[i]
            if in_range(cnh,cny,H,Y) and yard[cnh][cny] == 1 and visited[cnh][cny] == 0:
                visited[cnh][cny] = 1
                dq.append((cnh,cny))
    count += 1

#배추 위치 입력
for _ in range(T):
    Y, H, K = map(int, input().split())
    #사전 세팅
    yard = [[0]* Y for _ in range(H)]
    visited = [[0]* Y for _ in range(H)]
    count = 0
    for _ in range(K):
        h, y = map(int, input().split())
        yard[y][h] = 1
    
    for h in range(H):
        for y in range(Y):
            if yard[h][y] == 1 and visited[h][y] == 0:
                bfs(h,y)

    print(count)