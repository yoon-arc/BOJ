N = int(input())
o = input()
p = input()
ans = 0
for i in range(N):
    if o[i] == p[i]: ans += 1
print(ans)