N, M = map(int, input().split())
poke_num = {}
poke_name = {}

for i in range(1,N+1):
    name = input()
    poke_num[i] = name
    poke_name[name] = i

for i in range(M):
    now = input()
    if now.isdigit():
        print(poke_num[int(now)])
    else:
        print(poke_name[now])