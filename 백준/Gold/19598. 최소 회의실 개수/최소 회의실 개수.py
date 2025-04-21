import heapq

#회의의 수
N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
meetings.sort()
max_rooms = 0

#회의실
rooms = []

#회의 시작 시간과 끝나는 시간 입력
for s,e in meetings :
    
    while rooms and rooms[0] <= s:
        heapq.heappop(rooms)

    heapq.heappush(rooms,e)
    max_rooms = max(max_rooms, len(rooms))
    
# print(rooms)
print(max_rooms)   
        