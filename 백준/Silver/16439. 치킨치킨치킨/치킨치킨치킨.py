from itertools import combinations
#N명의 회원 M가지 종류
N, M = map(int, input().split())
chickens = [list(map(int, input().split())) for _ in range(N)]
max_sat = 0
#N명의 회원들이 1~3개의 치킨을 골랐을 때 만족도가 제일 높은 것(인덱스로 빼오기)
for chicken_comb in combinations(range(M),3): #range(M) = 치킨 번호/에서 3개를 고르는 경우의 수
    # print(chicken_comb)
    total_sat = 0
    #제일 높은거
    for chicken in chickens:
        # print(chicken)
        total_sat += max(chicken[i] for i in chicken_comb)

    max_sat = max(max_sat, total_sat)

print(max_sat)