N, K = map(int, input().split())
ans = []
for i in range(1, N+1):
    c = str(i)
    if c[-1] == str(K)[-1] or c[-1] == str(2*K)[-1]:
        continue
    ans.append(i)
ans.sort()
print(len(ans))
print(*ans)