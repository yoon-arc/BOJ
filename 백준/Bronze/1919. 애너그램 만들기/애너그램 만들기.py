a = list(input())
b = list(input())
ans = []
# #공통 되는 요소 찾기
inter = list(set(a) & set(b))
for i in range(len(inter)):
    ans += [inter[i]] * min(a.count(inter[i]), b.count(inter[i]))
#제외하기
for i in ans:
    a.remove(i)
    b.remove(i)
print(len(a)+len(b))