N = int(input())
Nlist = list(map(int, input().split()))
cards = {}
for i in Nlist:
    key = str(i)
    if key not in cards:
        cards[key] = 1
    else:
        cards[key] += 1
    #key값 문자열인거 헷갈리지 말기
M = int(input())
check = list(map(int, input().split()))
ans = []
for i in check:
    key = str(i)
    if key in cards:
        ans.append(cards[key])
    else:
        ans.append(0)
print(*ans)