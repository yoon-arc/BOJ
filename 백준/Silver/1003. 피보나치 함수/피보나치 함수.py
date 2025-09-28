import sys
input = sys.stdin.readline
#ibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지
T = int(input())
#0과 1이 호출된 횟수를 저장
count_zero = [0]*41
count_one = [0]*41
#초깃값
count_zero[0] = 1
count_one[1] = 1
#피보나치 값 계산
for i in range(2,41):
    count_zero[i] = count_zero[i-1]+count_zero[i-2]
    count_one[i] = count_one[i-1]+count_one[i-2]
#값 출력
for _ in range(T):
    num = int(input())
    print(count_zero[num], count_one[num])