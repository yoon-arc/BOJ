N = int(input())
ans_list = []
for i in range(1,N):
    if i + sum(map(int, str(i))) == N:
        ans_list.append(i)
print(min(ans_list) if ans_list else 0)