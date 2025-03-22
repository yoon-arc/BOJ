N = int(input())
dp = [0] * (N + 1)
dp[1] = 1
if N >= 2:
    dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007  # 문제에 따라 나머지 연산 적용

print(dp[N])