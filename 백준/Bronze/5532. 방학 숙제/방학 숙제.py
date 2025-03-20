import math

# 총 방학 날짜를 입력받습니다.
L = int(input())  
# 풀어야 하는 국어 페이지 수를 입력받습니다.
A = int(input())  
# 풀어야 하는 수학 페이지 수를 입력받습니다.
B = int(input())  
# 하루에 풀 수 있는 국어 페이지 수를 입력받습니다.
C = int(input())  
# 하루에 풀 수 있는 수학 페이지 수를 입력받습니다.
D = int(input())

# 국어 과목을 모두 풀기 위해 필요한 최소 날짜 계산 (올림 처리)
days_kor = math.ceil(A / C)
# 수학 과목을 모두 풀기 위해 필요한 최소 날짜 계산 (올림 처리)
days_math = math.ceil(B / D)

# 두 과목 중 더 많은 날짜가 소요되는 경우가 실제 필요한 날짜입니다.
min_required_days = max(days_kor, days_math)

# 남은 방학 날짜 계산 후 출력
print(L - min_required_days)
