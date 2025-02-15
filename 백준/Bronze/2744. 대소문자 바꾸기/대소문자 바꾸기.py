s = input()
new = ""

for i in s:
    if i.isupper():
        i = i.lower()
        new += i
    else:
        i = i.upper()
        new += i
        
print(new)