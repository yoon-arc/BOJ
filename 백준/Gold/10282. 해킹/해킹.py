import heapq
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

    # INF를 사용해 아직 감염되지 않은 상태를 표현
    INF = 10**9
    dist = [INF] * (n+1)
    dist[c] = 0
    
    # heapq를 큐로 사용 ( (감염 시간, 컴퓨터 번호) )
    heap = [(0, c)]
    
    while heap:        
        # print(f"현재 컴터는 {curr}")
        curr_time, curr = heapq.heappop(heap)
        if curr_time != dist[curr]:
            continue
        for connected, time in computers[curr]:
            can_time = curr_time + time  # curr를 통해 connected로 감염되는 시간
            if can_time < dist[connected]:
                dist[connected] = can_time
                heapq.heappush(heap, (can_time, connected))

    # INF가 아닌(감염된) 컴퓨터들의 감염 시간을 모음
    infected_times = [time for time in dist[1:] if time != INF]
    total_infected = len(infected_times)
    total_time = max(infected_times) if infected_times else 0
    print(total_infected, total_time)   