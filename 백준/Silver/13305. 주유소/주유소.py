#1km당 1리터. 각 도시에는 1개의 주유소, 가격 상이
N = int(input())
roads = list(map(int, input().split()))
fuel = list(map(int, input().split()))
now = fuel[0]
total = fuel[0]*roads[0]
for i in range(1,N-1):
    #새로운 최저가 주유소 발견
    if fuel[i] < now:
        now = fuel[i]
    total += now*roads[i]
print(total)