T = int(input())
for _ in range(T):
    s = input()
    if s[-1:] != '.':
        s += '.'
    print(s)