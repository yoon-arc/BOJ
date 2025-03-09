#스위치 수 
N = int(input())
#스위치들
switch = [0] + list(map(int, input().split()))
#학생 수
S = int(input())
#[[성별, 받은 수],[성별, 받은 수]]
students = []
for _ in range(S):
    students.append(list(map(int, input().split())))


#students[i][0] == 1 (남학생 경우)
def when_boy(num):
    for i in range(num, N+1):
        if (i)%num == 0:
            switch[i] = 1 - switch[i]
    
#students[i][0] == 2 (여학생 경우)
def when_girl(num):
    switch[num] = 1-switch[num]
    left = num -1
    right = num + 1
    while left >= 1 and right <= N and switch[left] == switch[right]:
        switch[left] = 1 - switch[left]
        switch[right] = 1 - switch[right]
        left -= 1
        right += 1

for gender, num in students:
    if gender == 1:
        when_boy(num)
    if gender == 2:
        when_girl(num)
    
ans = switch[1:]
# print(len(ans))
for i in range(len(ans)):
    if i % 20 == 0 and i != 0:
        print(end='\n')
    print(ans[i], end=" ")