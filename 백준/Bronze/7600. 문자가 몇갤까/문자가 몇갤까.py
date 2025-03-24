going = True

while going:
    stack = []
    count = 0
    c = list(input())
    if c[0] == '#':
        going = False
        break
        
    for i in c:
        if i.lower() not in stack and i.isalpha():
            count += 1
            stack.append(i.lower())
            # print(i)
        else:
            continue
    print(count)