import sys
input = sys.stdin.readline
plates = input().strip()
total = 10
for i in range(1, len(plates)):
    if plates[i] == plates[i-1]:
        total += 5
    else:
        total += 10
print(total)