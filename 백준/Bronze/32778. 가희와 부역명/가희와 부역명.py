word = list(input())
i = 0
first = ""
secound = ""
while i < len(word) and word[i] != '(':
    first += word[i]
    i += 1
    
if '(' in word:
    si = word.index('(')
    ei = word.index(')')
    secound = ''.join(word[si+1:ei])
else:
    secound = '-'
print(f"{first}\n{secound}")