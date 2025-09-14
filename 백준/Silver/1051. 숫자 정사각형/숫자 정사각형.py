N, M = map(int, input().split())
rect = [list(input().strip()) for _ in range(N)]
ans = 0
check = min(N,M)

for h in range(N):
    for y in range(M):
        for n in range(check):
            if (h+n)<N and (y+n)<M and rect[h][y] == rect[h][y+n] == rect[h+n][y] == rect[h+n][y+n]:
                ans = max(ans, ((n+1)**2))
print(ans)