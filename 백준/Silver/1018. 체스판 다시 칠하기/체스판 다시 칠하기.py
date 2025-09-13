N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
min_paint = 64

rowW = "WBWBWBWB"
rowB = "BWBWBWBW"

for h in range(N-7):#창의 시작 행
    for y in range(M-7):#창의 시작 열
        count_W = 0
        count_B = 0
        curW, curB = rowW, rowB

        for r in range(8):
            now = board[h+r][y:y+8]
            # print(now)
            #비교하며 반복
            for a,b in zip(now,curW):
                if a!=b:
                    count_W += 1
            for a,b in zip(now,curB):
                if a!=b:
                    count_B += 1
            #다음행 템플릿 뒤집기
            curW, curB = curB, curW
        min_paint = min(min_paint, count_W, count_B)
print(min_paint)