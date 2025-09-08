# N = abc + a + b + c
N = int(input())
numList = []
for i in range(1, N):
    if i + sum(map(int, str(i))) == N:
        numList.append(i)

if numList :
    print(min(numList))
else:
    print(0)