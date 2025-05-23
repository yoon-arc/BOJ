N = int(input())
for _ in range(N):
    ans = 0
    A,B,C,D,E = map(float, input().split())
    ans += A*350.34 + B*230.90 + C*190.55 + D*125.30 + E*180.90
    print(f"${ans:.2f}")