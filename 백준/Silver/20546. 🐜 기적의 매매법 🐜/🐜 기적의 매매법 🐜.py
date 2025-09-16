money = int(input())
rates = list(map(int, input().split()))

def jun(m, r):
    total = 0
    for stock in r:
        if m >= stock:
            amount = m//stock
            total += amount
            m -= stock*amount
    return (total*r[-1])+m
    
def sung(m, r):
    total = 0
    up = down = 0
    for i in range(1, len(r)):
        if r[i] > r[i-1]:
            up += 1
            down = 0
        elif r[i-1] > r[i]:
            down += 1
            up = 0
        else:
            up = down = 0
        
        if down >= 3:
            amount = m // r[i]
            total += amount
            m -= r[i]*amount
        if total and up >= 3:
            m = total * r[i]
            total = 0
        else:
            continue
    return (total*r[-1])+m
    
j = jun(money,rates)
s = sung(money,rates)
# print(j,s)
if j > s:
    print('BNP')
elif s > j:
    print('TIMING')
else:
    print('SAMESAME')