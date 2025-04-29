N, M = map(int, input().split())
people = {}
ans = []
for _ in range(N):
    name = input()
    people[name] = 1
for _ in range(M):
    name = input()
    if name in people :
        people[name] = 2

for name in people:
    if people[name] == 2:
        ans.append(name)
print(len(ans))
ans.sort()
for n in ans:
    print(n)