T = int(input())

# def GCD():
def GCD(a,b):
    while b:
        a, b = b, a % b
    return a
    
for _ in range(T):
    a, b = map(int, input().split())
    g = GCD(a,b)
    l = (a*b) // g
    print(l,g)