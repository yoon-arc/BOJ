n = int(input())
cards = list(map(int, input().split()))
cards.sort(reverse=True)
total = 0
for i in range(1,n):
    total += cards[0]+cards[i]
    # print(f"현재 총 값은{total}, {cards[0]}에 {cards[i]}더하는 중")
print(total)