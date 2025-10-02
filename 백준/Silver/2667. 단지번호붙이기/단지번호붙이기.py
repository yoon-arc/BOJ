from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
apts = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dh, dy = [-1,0,1,0],[0,1,0,-1]
nums = []

def in_range(h,y,N):
    return 0<= h < N and 0<= y < N

def bfs(h, y):
    dq = deque([])
    dq.append([h,y])
    visited[h][y] = 1
    count = 1
    while dq:
        now = dq.popleft()
        nh, ny = now[0], now[1]
        for i in range(4):
            chs, cys = nh+dh[i], ny+dy[i]
            if in_range(chs, cys,N) and apts[chs][cys]== 1 and visited[chs][cys] == 0:
                visited[chs][cys] = 1
                dq.append([chs, cys])
                count += 1
    nums.append(count)
                
        

for h in range(N):
    for y in range(N):
        # print(h,y)
        if apts[h][y] == 1 and visited[h][y] == 0:
            bfs(h,y)

nums.sort()
print(len(nums))
for i in nums:
    print(i)