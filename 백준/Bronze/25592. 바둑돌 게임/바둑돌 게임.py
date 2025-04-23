N = int(input())
#홀수 번대를 확인
turn = 0

while N > turn:
    turn += 1
    N -= turn
    
if turn % 2 == 1:
    print(0)
else:
    print((turn+1)-N)