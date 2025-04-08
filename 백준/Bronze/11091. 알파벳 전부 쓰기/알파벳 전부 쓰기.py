alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
N = int(input())
for _ in range(N):
    alp_stack = alp.copy()
    s = input().replace(" ","")
    for i in s:
        if i.isupper():
            i = i.lower()
        if i in alp_stack:
            alp_stack.remove(i)
    if alp_stack:
        print('missing',"".join(alp_stack))
    else:
        print('pangram')