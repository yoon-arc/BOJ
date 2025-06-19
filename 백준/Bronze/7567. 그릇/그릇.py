plates = input()
total = 10
for i in range(1, len(plates)):
    if plates[i] == plates[i-1]:
        total += 5
    else:
        total += 10
print(total)