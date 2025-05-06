N = int(input())
dp = [0,-1,-1,1,-1,1,2,-1] + [0]*(N+2)
for i in range(8, N+1):
    if i < 15 and i % 3 == 0:
        dp[i] = dp[i-3]+1
    else:
        dp[i] = dp[i-5]+1
print(dp[N])