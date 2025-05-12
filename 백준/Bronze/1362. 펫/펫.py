scenario = 0
while True:
    o, w = map(int, input().split())
    #0,0입력 시 종료
    if o == 0 and w == 0:
        break
    #시나리오 값 증가
    scenario += 1
    status = ""
    while True:
        C, S = input().split()
        S = int(S)
        #사이클 종료
        if C == '#' and S == 0:
            if status == 'RIP':
                print(scenario, status)
            else:
                print(scenario, ':-)' if o//2< w < o*2 else ':-(')
            break
        if w > 0:
            if C == 'E':
                w -= S
            if C == 'F':
                w += S
        if w <= 0 :
            status = "RIP"