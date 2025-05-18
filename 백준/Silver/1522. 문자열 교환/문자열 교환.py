S = input()
N = len(S)
r = S.count('a')
SS = S + S
min_b = N

for i in range(N):
    n = SS[i:i+r].count('b')
    if n < min_b:
        min_b = n
print(min_b)