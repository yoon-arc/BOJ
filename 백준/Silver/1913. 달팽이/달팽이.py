N = int(input())
find = int(input())
snail = [[0]*N for _ in range(N)]
dh, dy = [1,0,-1,0],[0,1,0,-1]
count = N**2
h, y = 0,0
#아래를 향하고 있음
nd = 0
locH, locY = 0,0
#반시계 회전(n-1+4)%4
def in_range(h,y):
    return 0<= h < N and 0<= y <N

while count >= 1:
    snail[h][y] = count
    if count == find:
        locH, locY = h+1, y+1
        
    nh, ny = h+dh[nd], y+dy[nd]
    if not in_range(nh, ny) or snail[nh][ny] != 0:
        nd = (nd+1)%4
        nh, ny = h+dh[nd], y+dy[nd]
    h, y = nh, ny   
    count -= 1

            
# print(*snail)
for row in snail:
    print(*row)
print(locH, locY)