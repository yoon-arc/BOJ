N = int(input())
houses = sorted(map(int, input().split()))
print(houses[(N-1)//2])