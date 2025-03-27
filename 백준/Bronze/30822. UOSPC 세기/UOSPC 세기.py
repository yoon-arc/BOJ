N = int(input())
word = input()
maxN = 1000000
p = "uospc"

for i in p:
    n = word.count(i)
    if n < maxN:
        maxN = n
print(maxN)