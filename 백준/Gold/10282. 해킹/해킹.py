from collections import deque
#테스트 케이스
t = int(input())
for _ in range(t):
    # n = 컴퓨터 수, d = 의존성(연결된 에지 수), c = 시작점
    n, d, c = map(int, input().split())
    #에지 수에 따라 미리 형성
    computers = {i:[] for i in range(n+1)}

    #컴퓨터 정보 입력
    for _ in  range(d):
        #a,b,s = a가 b에 의존, 에지 가중치 s
        a,b,s = map(int, input().split())
        computers[b].append((a, s))

    #감염 시간
    dist = [None] * (n+1)
    dist[c] = 0    
    #큐
    dq = deque([c])
    
    while dq:
        curr = dq.popleft()
        # print(f"현재 컴터는 {curr}")
        for connected, time in computers[curr]:
            can_time = dist[curr] + time  # curr를 통해 걸리는 시간
            #아직 감염되지 않았거나 최적 시간 발견 시
            if dist[connected] is None or can_time < dist[connected]:
                dist[connected] = can_time
                dq.append(connected)

    infected_times = []
    for time in dist:
        if time is not None:
            infected_times.append(time)
    #결괏값
    total_infected = len(infected_times)
    total_time = max(infected_times)
    print(total_infected, total_time)        