# 유진수
N = input()
lenN = len(N)
count = 1
ans = 0

if not lenN == 1:
    for i in range(lenN):
        rest = 1
        count *= int(N[i])
        for j in range(i+1,lenN):
            rest *= int(N[j])
        # print(f"현재 인덱스는{i} count는{count} rest는 {rest}")
        if count == rest:
            print("YES")
            ans = 1
            break

if not ans:
    print("NO")