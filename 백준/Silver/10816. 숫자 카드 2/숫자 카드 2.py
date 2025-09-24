from collections import Counter
import sys
N = int(input())
Ndic = Counter(map(int, sys.stdin.readline().split()))
M = int(input())
Mlist = map(int, sys.stdin.readline().split())

for i in Mlist:
    print(Ndic[i], end=" ")

