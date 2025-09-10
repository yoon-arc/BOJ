tri = [(i*(i+1))//2 for i in range(1,44)]

T = int(input())
for _ in range(T):
    ans = 0
    K = int(input())
    
    for f in tri:
        if ans == 1:
            break
        for s in tri:
            if ans == 1:
                break
            for h in tri:
                if f+s+h == K:
                    ans = 1 
                if ans == 1:
                    break

    print(ans) 