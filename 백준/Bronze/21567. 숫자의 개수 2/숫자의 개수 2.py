import math
nums = list(int(input()) for _ in range(3))
a = str(math.prod(nums))
for i in range(10):
    print(a.count(str(i)))