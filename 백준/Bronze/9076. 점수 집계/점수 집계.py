import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    nums.sort()
    if nums[-2] - nums[1] >= 4:
        print('KIN')
        continue
    else:
        print(sum(nums[1:-1]))