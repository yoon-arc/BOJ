T = int(input())
for _ in range(T):
    N = input()
    if (int(N)+1) % int(N[2:]) == 0:
        print('Good')
    else:
        print('Bye')