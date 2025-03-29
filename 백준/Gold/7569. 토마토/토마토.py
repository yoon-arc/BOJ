#최소 걸리는 날짜 구하기
from collections import deque 
#큐
dq = deque([])
#토마토가 담기는 상자
box = []
# 총 걸리는 날짜
days = 0

#검사 방향 (상,우,하,좌,z위, z 아래)
dh, dn, dm = [0,0,0,0,-1,1],[-1,0,1,0,0,0],[0,1,0,-1,0,0]
#N = 행, M = 열, H = 층
M, N, H = map(int, input().split())

#초기 토마토 받기
for _ in range(H):
    floor = [list(map(int, input().split())) for _ in range(N)]
    box.append(floor)


#시작 위치 좌표를 큐에 넣기(h,n,m)

# #bfs함수
def bfs():
    #큐에 값이 있는 동안
    while dq:
        # print(dq)
    #4번을 뒤져가며 익힐 토마토를 찾음
        h,n,m = dq.popleft()
        # print(h,n,m)
        for i in range(6):
            dnh , dnn, dnm = dh[i],dn[i],dm[i]
            nh = h + dnh
            nn = n + dnn
            nm = m + dnm
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
                if box[nh][nn][nm] == 0:
                    box[nh][nn][nm] = box[h][n][m] + 1
                    dq.append([nh,nn,nm])
        
#시작 지점
for h in range(H):
    for n in range(N):
        for m in range(M):
            #특정 토마토
            if box[h][n][m] == 1:
                dq.append([h,n,m])

bfs()

#최종 검사
for h in range(H):
    for n in range(N):
        if 0 in box[h][n]:
            print(-1)
            exit()
        days = max(days, max(box[h][n]))

print(days-1)