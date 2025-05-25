import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for i in range(N):
    word = input().rstrip()
    if len(word) >= M :
        if word not in dic :
            dic[word] = 1
        else:
            dic[word] += 1
f = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for w in f:
    print(w[0])