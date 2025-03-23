M, N = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(M)]
d = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
count = 0
# print(banner)
def find_letter(h,y):
    stack = [(h,y)]
    #연결된 모든 글자를 찾고, 1이면 0으로 전환
    while stack:
        ch, cy = stack.pop()
        if banner[ch][cy] == 0:
            continue
        #방문처리
        banner[ch][cy] = 0
        for ph, py in d:
            mh, my = ch+ph, cy+py
            if 0<= mh < M and 0<=my<N and banner[mh][my]:
                stack.append((mh, my))
for h in range(M):
    for y in range(N):
        now = banner[h][y]
        if now == 1:
            count += 1
            find_letter(h,y)

print(count)