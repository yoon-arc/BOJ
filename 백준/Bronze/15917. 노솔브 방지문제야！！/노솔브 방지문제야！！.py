import sys
input = sys.stdin.readline
Q = int(input())
for _ in range(Q):
    a = int(input())
    if a == 1:
        print(1)
    else:
        # 2로 나누면서, 나누어 떨어지지 않으면 2의 거듭제곱이 아님
        while a % 2 == 0:
            a //= 2  # 2로 나누기
        
        # 마지막에 1이 되면 2의 거듭제곱, 아니면 0 출력
        if a == 1:
            print(1)
        else:
            print(0)
        