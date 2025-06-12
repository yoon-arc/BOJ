import math
N = int(input())
scores = [input() for _ in range(N)]
total = 0
for i in scores:
    if i == '100':
        total += 100
        continue
    total += int(i.replace('0', '9').replace('6', '9'))
print(math.floor((total/N)+ 0.5))