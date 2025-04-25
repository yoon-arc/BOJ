words = {'H':0, 'I':0, 'A':0, 'R':0, 'C':0}
N = int(input())
e = input()
for i in e:
    if i in words:
        words[i] += 1
min_key = min(words, key=words.get)
print(words[min_key])