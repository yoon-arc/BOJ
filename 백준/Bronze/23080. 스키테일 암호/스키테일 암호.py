K = int(input())
s = input()
ans = ''
for i in range(0,len(s),K):
    ans += s[i]
print(ans)