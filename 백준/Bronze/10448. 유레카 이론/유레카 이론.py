tri = [(i*(i+1))//2 for i in range(1,45)]

T = int(input())
for _ in range(T):
    ans = 0
    K = int(input())
    
    for f in tri:
        if f > K: break
        if ans : break
        for s in tri:
            if f+s > K : break
            for h in tri:
                if f+s+h == K:
                    ans = 1 
                    break
            if ans : break

    print(ans)    