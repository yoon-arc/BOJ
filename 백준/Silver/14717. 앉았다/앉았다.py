import itertools

def getScore(a,b):
    if a==b:
        return (2,a)
    else:
        return (1,(a+b)%10)

cards = [i for i in range(1, 11)] * 2
A, B = map(int, input().split())

sA = getScore(A,B)
#카드 제거
cards.remove(A)
cards.remove(B)
nCr = itertools.combinations(cards,2)

win = 0
total_round = 0
for x,y in nCr:
    total_round += 1
    sB = getScore(x,y)
    if sA > sB:
        win += 1
    else:
        continue
print(f"{win/total_round:0.3f}")