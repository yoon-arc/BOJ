from itertools import combinations 
L , C = map(int, input().split())
m = ['a', 'e', 'i', 'o', 'u']
keys = list(input().split())
keys.sort()
# print(keys)

for w in range(C-L+1):
    nCr = list(combinations(keys,L))

for c in nCr:
    c = list(c)
    if c == sorted(c):
        totalM = 0
        for i in m:
            totalM += c.count(i)
            # print(totalM)
        if totalM >= 1 and len(c)-totalM >=2:
            print("".join(c))
    