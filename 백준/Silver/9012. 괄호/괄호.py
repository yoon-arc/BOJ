T = int(input())
for _ in range(T):
    line = list(input())
    ans = []
    for i in line:
        if i == ')' and not ans:
            ans.append(')')
            break
        if i == '(':
            ans.append('(')
        else:
            ans.pop()
    if ans :
        print('NO')
    else:
        print('YES')