N,M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = grid[0][0]

for i in range(0,N):
    for j in range(0,M):
        if i+1 < N and j+1<M:
            dp[i+1][j+1] = max(dp[i][j]+ grid[i+1][j+1], dp[i+1][j+1])
        if i+1 < N:
            dp[i+1][j] = max(dp[i][j]+grid[i+1][j], dp[i+1][j])
        if j+1 < M:
            dp[i][j+1] = max(dp[i][j]+grid[i][j+1], dp[i][j+1])
print(dp[N-1][M-1])