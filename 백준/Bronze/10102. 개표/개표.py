V = int(input())
result = list(input())
if result.count('A') > result.count('B'):
    print('A')
elif result.count('A') < result.count('B'):
    print('B')
else:
    print('Tie')