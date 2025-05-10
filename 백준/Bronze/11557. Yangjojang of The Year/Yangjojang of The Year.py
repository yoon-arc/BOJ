T = int(input())
for _ in range(T):
    N = int(input())
    max_school = -1
    max_name = ""
    for _ in range(N):
        info = list(input().split())
        if int(info[1]) > max_school:
            max_school = int(info[1])
            max_name = info[0]
    print(max_name)