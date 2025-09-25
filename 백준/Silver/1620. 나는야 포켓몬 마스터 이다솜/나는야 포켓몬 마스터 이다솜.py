import sys
input = sys.stdin.readline

M, N = map(int, input().split())
num_to_name = {}
name_to_num = {}

# 포켓몬 도감 등록
for i in range(1, M + 1):
    name = input().rstrip()
    num_to_name[i] = name
    name_to_num[name] = i

# 문제 출력
for _ in range(N):
    query = input().rstrip()
    if query.isdigit():
        print(num_to_name[int(query)])
    else:
        print(name_to_num[query])