N = int(input())
T = [0]*(N)
P = [0]*(N)
for i in range(N):
    T[i], P[i] =  map(int, input().split())


def dfs(e, amount):
    global ans
    #종료 조건
    if e >= N :
        ans = max(ans, amount)
        return ans
    #만약 다음 날을 더한게 기간(N)을 넘지 않는다면
    if e + T[e] <= N:
        dfs(e+T[e], amount+P[e])
    #스킵
    dfs(e+1, amount)

ans = 0
dfs(0, 0)
print(ans)