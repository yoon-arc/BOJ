N = int(input())
T = [0]*(N+1) #기간
P = [0]*(N+1) # 비용
for i in range(1, N+1):
    t, p = map(int, input().split())
    T[i], P[i] = t, p
#dp 테이블    
dp = [0]*(N+2)

for i in range(1, N+1):
    dp[i+1] = max(dp[i+1], dp[i])
    #갱신
    check = T[i] + i
    if check <= N+1:
        dp[check] = max(dp[i] + P[i] , dp[check])
print(max(dp))