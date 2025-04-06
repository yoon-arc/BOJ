# x, y 좌표, 한 블록 이동 시간, 대각선 이동 시간
X, Y, W, S = map(int, input().split())

# 직선 이동만 하는 경우(대각선이 비효율적일떄)
option1 = (X + Y) * W

# 대각선 이동 후, 직선 이동(정사각형 처리 후 남은 거)
option2 = min(X, Y) * S + abs(X - Y) * W

#모양이 정사각형이라 전부 대각선 이동이 된다면??? 
if abs(X - Y) % 2 == 0:
    option3 = max(X, Y) * S
else:#마지막만 처리
    option3 = (max(X, Y) - 1) * S + W

ans = min(option1, option2, option3)
print(ans)
