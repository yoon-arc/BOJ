def camel_case(letters):
    c_letter = letters[0]
    for i in range(1, len(letters)):
        c_letter += letters[i][0].upper()+letters[i][1:]
    print(c_letter)
def snake_case(letters):
    c_letter = '_'.join(letters)
    print(c_letter)
def pascal_case(letters):
    c_letter = ""
    for i in letters:
        c_letter += i[0].upper()+i[1:]
    print(c_letter)

N, L = input().split()
#카멜
if N == "1":
    letters = []
    letter = ""
    for i in L:
        if i.islower():
            letter += i
        if i.isupper():
            letters.append(letter)
            letter = i.lower()
    letters.append(letter.lower())
    #출력
    print(L)
    snake_case(letters)
    pascal_case(letters)
    
#스네이크
elif N == "2":
    letters = L.split('_')
    #출력
    camel_case(letters)
    print(L)
    pascal_case(letters)
    
#파스칼
else:
    letters = []
    letter = ""
    for i in L:
        if i.isupper():
            letters.append(letter)
            letter = i.lower()
            continue
        letter += i.lower()
    letters.append(letter)
    #출력
    camel_case(letters[1:])
    snake_case(letters[1:])
    print(L)