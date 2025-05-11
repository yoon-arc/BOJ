#1km당 1리터. 각 도시에는 1개의 주유소, 가격 상이
#최소 비용
N = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))
total = 0
for i in range(N-1):
    if cities[i] == min(cities[:-1]):
        for j in range(i, N-1):
            total += (cities[i]*roads[j])
        break
    else:
        total += cities[i]*roads[i]
    
print(total)