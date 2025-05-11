#국가의 수, 등수 알고싶은 나라
N, K = map(int, input().split())
countries = []
count = 1
#입력
for i in range(N):
    num, g,s,b = map(int, input().split())
    countries.append([num,g,s,b])
#정렬
countries.sort(key = lambda x : (-x[1],-x[2],-x[3]))
#동점 처리
for i in range(len(countries)):
    if countries[i][0] == K:
        if countries[i-1][1:] == countries[i][1:]:
            count -= 1
        print(count)
        break
    count += 1
