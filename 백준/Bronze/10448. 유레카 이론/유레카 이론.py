def get_ans(f,s,h):
    return 1 if (f*(f+1)//2) + (s*(s+1)//2)+ (h*(h+1)//2)==K else 0

T = int(input())
for _ in range(T):
    ans = 0
    K = int(input())
    
    for f in range(1,46):
        if ans == 1:
            break
        for s in range(1,46):
            if ans == 1:
                break
            for h in range(1,46):
                ans = get_ans(f,s,h)
                if ans == 1:
                    break

    print(ans)    