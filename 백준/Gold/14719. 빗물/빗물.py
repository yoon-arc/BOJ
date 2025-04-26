H, W = map(int, input().split())
info = list(map(int, input().split()))
blocks = [list(0 for _ in range(W))for _ in range(H)]
count = 0
for i in range(len(info)):
    c = info[i]
    for y in range(H-1, H-c-1, -1):
         blocks[y][i] = 'x'
for h in range(H):
    for y in range(W):
        if blocks[h][y] == 'x' and y != W-1 and blocks[h][y+1] != 'x':
            temp_count = 0
            for ny in range(y+1, W):
                if blocks[h][ny] == 'x':
                    count += temp_count
                    break
                else:
                    temp_count += 1
print(count)