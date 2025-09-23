import sys
input = sys.stdin.readline

N = int(input())
people = {}

for _ in range(N):
    name, log = input().split()
    if log == 'enter':
        people[name] = True
    else:  # 'leave'
        people.pop(name, None)
for name in sorted(people.keys(), reverse=True):
    print(name)