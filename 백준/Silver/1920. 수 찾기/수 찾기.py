import sys
N = int(input())
nList = set(map(int, sys.stdin.readline().split()))
M = int(input())
mList = list(map(int, sys.stdin.readline().split()))

for i in mList:
    if i in nList:
        print(1)
    else:
        print(0)