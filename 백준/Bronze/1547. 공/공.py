M = int(input())
cups = [1,2,3]
ball = 1
for _ in range(M):
    a, b = map(int, input().split())
    if ball == a: ball = b
    elif ball == b: ball = a
print(ball)