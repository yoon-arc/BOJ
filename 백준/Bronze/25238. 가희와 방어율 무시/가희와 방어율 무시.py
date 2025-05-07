a, b = map(int, input().split())
total = int(a - (a * (b/100)))
print(0 if total >= 100 else 1)