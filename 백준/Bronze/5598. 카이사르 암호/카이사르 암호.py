word = list(input())
for w in word:
    if ord(w)<68:
        c = ord(w)+23
        print(chr(c), end="")
    else:
        c = ord(w)-3
        print(chr(c), end="")