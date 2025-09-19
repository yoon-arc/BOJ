from itertools import combinations

def cal(team1, team2):
    a = b = 0
    for i in range(len(team1)):
        for j in range(len(team1)):
            a += S[team1[i]][team1[j]]
            b += S[team2[i]][team2[j]]
    return abs(a - b)

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

people = list(range(N))
ans = float('inf')

for team1 in combinations(people, N // 2):
    team2 = list(set(people) - set(team1))
    diff = cal(team1, team2)
    ans = min(ans, diff)
    if ans == 0:
        break  # 최소가 0이면 더 볼 필요 없음

print(ans)
