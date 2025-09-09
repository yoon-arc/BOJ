import itertools
dwarfs = []
for i in range(9):
    dwarf = int(input())
    dwarfs.append(dwarf)

seven = list(itertools.combinations(dwarfs,7))

for i in seven:
    if sum(i) == 100:
        print(*sorted(i), sep='\n')
        break