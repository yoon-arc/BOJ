#국가의 수, 등수 알고싶은 나라
N, K = map(int, input().split())
countries = []
#입력
for i in range(N):
    num, g,s,b = map(int, input().split())
    countries.append([num,g,s,b])
#정렬
countries.sort(key = lambda x : (-x[1],-x[2],-x[3]))
#출력(동점 처리 포함)
rank = 1
pg, ps, pb = 0,0,0
for idx, (n,g,s,b) in enumerate(countries):
    if idx == 0:
        prev_medals = (g, s, b)
    #메달 조합이 바뀌었을 때만
    else: 
        if(g,s,b) != (pg,ps,pb):
            rank = idx + 1
            pg,ps,pb = g,s,b
    if n == K:
        print(rank)
        break