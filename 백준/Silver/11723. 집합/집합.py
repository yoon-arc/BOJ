import sys
input = sys.stdin.readline

M = int(input())
ALL = set(range(1, 21))
s = set()
for _ in range(M):
    now = input().split()
    cmd = now[0]
    if cmd == "add":
        s.add(int(now[1]))
    elif cmd == "remove":
        s.discard(int(now[1]))
    elif cmd == 'check':
        if int(now[1]) in s:
            print("1")
        else:
            print("0")
    elif cmd == 'toggle':
        if int(now[1]) in s:
            s.discard(int(now[1]))
        else:
            s.add(int(now[1]))
    elif cmd == 'all':
        s = ALL.copy()
    elif cmd == 'empty':
        s.clear()
