import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
Ndic = Counter(map(int, input().split()))
M = int(input())
Mdic = list(map(int, input().split()))
for i in Mdic:
    print(Ndic[i] , end=" ")