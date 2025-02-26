T = int(input())
cases = [int(input()) for _ in range(T)]
D = [0] * (max(cases)+1)
D[1],D[2],D[3] = 1,2,4

# def get_cases(c):
#     for i in range

for c in cases:
    for i in range(3,c+1):
        if not D[i]:
            D[i] = D[i-1]+D[i-2]+D[i-3]
    print(D[c])
        