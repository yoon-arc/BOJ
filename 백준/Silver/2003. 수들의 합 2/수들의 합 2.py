N, M = map(int, input().split())
nums = list(map(int, input().split()))
total = 0

for i in range(N):
    count = 0
    j = i
    while j < N:
        count += nums[j]
        j += 1
        
        if count == M :
            total += 1
            break
            # print(f"{j}인덱스")
    # total += 1
print(total)