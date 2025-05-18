import sys
input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))

left, right = 0, N-1
best = liquids[left] + liquids[right]

while left < right:
    current = liquids[left] + liquids[right]
    if abs(current) < abs(best):
        best = current

    if current < 0 :
        left += 1
    else:
        right -= 1
print(best)