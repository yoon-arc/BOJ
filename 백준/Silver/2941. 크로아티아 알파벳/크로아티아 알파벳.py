alp = {'c=':'č','c-':'ć','dz=':'dž', 'd-':'đ','lj':'lj','nj':'nj','s=':'š','z=':'ž'}
count = 0
word = input()
chance = len(word)
curr = 0

while curr < chance:
    # 'dz=' 처리
    if curr < chance - 2 and word[curr] == 'd' and word[curr+1] == 'z' and word[curr+2] == '=':
        count += 1
        curr += 3
    # 두 글자 크로아티아 문자 처리
    elif curr < chance - 1 and word[curr] + word[curr+1] in alp:
        count += 1
        curr += 2  # 두 글자씩 건너뛰어야 하므로 curr += 2
    else:
        count += 1  # 한 글자 처리
        curr += 1

print(count)
